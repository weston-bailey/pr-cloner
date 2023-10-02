# PR Cloner

Tool to automate the process of cloning all open pull requests on a github repo

## Getting Started

* clone this repo and cd in the directory
* run `python3 -m venv venv` to create a virtual enviroment
* run  `source ./venv/bin/activate` to enter the virutal enviroment
* run `pip3 install -r requirements.txt` to install the required packages
* run `python3 main.py < owner name > < repo name > < auth method >` to run the script and clone all open prs on `< owner name >/< repo name >` using specified `< auth method >`
	* `< auth method >` defaults to `ssh` if ommited and can alternatively be `https`
	* open pull requests are cloned into `cloned_repos/< repo name >/< gh username >`

example usage: 
```sh
$ python3 main.py WDI-SEA sei-tic-tac-toe
repo owner: WDI-SEA, repo name: sei-tic-tac-toe, auth method: ssh
Cloning into 'Slmbyn'...

Cloning into 'ownerl'...

Cloning into 'mselbekk11'...

Cloning into 'lvlivingston'...

Cloning into 'caitlinfcorrigan'...

Cloning into 'MelanieWinter'...

Cloning into 'carldamey'...

Cloning into 'weston-bailey'...

Cloning into 'mHaines9219'......
...
```
