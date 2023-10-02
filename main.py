import os
import sys
from lib.Cloner import Cloner

def main():
    # if (len(sys.argv) < 2):
    #     raise Exception("script requires a valid github repo url to run!")
    REPO_URL = sys.argv[1]
    Cloner(REPO_URL)

if __name__ == "__main__":
    main()

