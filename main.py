import os
import sys
from lib.Cloner import Cloner

def main():
    try: 
        if len(sys.argv) < 3:
           Cloner.raise_exception() 

        REPO_OWNER, REPO_NAME = sys.argv[1], sys.argv[2]
        AUTH_METHOD = "ssh" if len(sys.argv) < 4 else sys.argv[3]
        cloner = Cloner(REPO_OWNER, REPO_NAME, AUTH_METHOD)

        print(cloner)        
        cloner.run()

    except Exception as e:
        print(e)
        print("""
Usage:
    python3 main.py "github owner/organization name" "github repository name" "(optional) auth method ('ssh or 'https')" 
    
Example Usages:
    python3 main WDI-SEA sei-tic-tac-toe
    > clones https://github.com/WDI-SEA/sei-tic-tac-toe/tree/main using ssh

    python3 main WDI-SEA sei-tic-tac-toe https
    > clones https://github.com/WDI-SEA/sei-tic-tac-toe/tree/main using https
            """)
    


if __name__ == "__main__":
    main()

