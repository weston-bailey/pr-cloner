import requests
import subprocess

class Cloner:
    """
    Tool to automate cloning all open pull requests on a specified github repository.\n
    cloner = Cloner(\n
        repo_owner: str = gh owner/organization, \n
        repo_name: str = name of repo to be cloned, \n
        auth_method: str = auth method used for cloner (defaults to "ssh", can also be "https")\n
    )\n
    cloner.run() -> self: clones all open pulls into cloned_repos/< repo_name >/< pr author name >
    """
    def __init__(self, repo_owner, repo_name, auth_method = "ssh"):
        self.__repo_owner = repo_owner
        self.__repo_name = repo_name
        self.__auth_method = auth_method
        if self.__auth_method not in ("ssh", "https"):
            raise Exception(f" Invalid auth method: {self.__auth_method}.Auth method must be either 'ssh' or 'https'.")

    def __repr__(self):
        return f"repo owner: {self.__repo_owner}, repo name: {self.__repo_name}, auth method: {self.__auth_method}"

    @staticmethod    
    def raise_exception():
            raise Exception("cloner requires a valid github repository owner repository name to run!")    

    def run(self):
        if not self.__repo_owner or not self.__repo_name:
            Cloner.raise_exception()

        # get all pulls regardless of how many there are
        page = 1
        pulls = []
        while True:
            response = requests.get(f"https://api.github.com/repos/{self.__repo_owner}/{self.__repo_name}/pulls?per_page=100&page={page}")
            response = response.json()
            if len(response) == 0:
                break
            pulls += response
            page += 1

        # extracted wanted data
        def map_url(pull):
            return { 
                "name": pull["user"]["login"], 
                "ssh_url": pull["head"]["repo"]["ssh_url"],
                "https_url": pull["head"]["repo"]["html_url"] + ".git"
            } 

        cloning_urls = list(map(map_url, pulls))

        # clone down all prs
        def run_subprocess(command):
            completed_process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if completed_process.returncode != 0:
                print(f"subprocess '{command}' gave non 0 exit code {completed_process.returncode}.")
            if completed_process.stderr:
                print(completed_process.stderr)
            if completed_process.stdout:
                print(completed_process.stdout)

            return completed_process

        run_subprocess(f"mkdir -p cloned_repos/{self.__repo_name}")

        for cloning_url in cloning_urls:
            clone_url_string = cloning_url[f"{self.__auth_method}_url"]
            run_subprocess(f"cd cloned_repos/{self.__repo_name} && git clone {clone_url_string} {cloning_url['name']}")

        return self


