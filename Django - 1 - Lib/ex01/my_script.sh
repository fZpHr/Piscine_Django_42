#!/bin/bash

# set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'

exec > path.log 2>&1

pipenv --rm 
pipenv install
pipenv run pip --version > /dev/null 2>&1
if [ $? -eq 0 ]; then
    pip_version=$(pipenv run pip --version)
    echo -e "${GREEN}Pip is installed: $pip_version${NC}"
else
    echo -e "${RED}Pip is not installed${NC}"
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    pipenv run python3 get-pip.py
    pipenv run python3 -m pip install --upgrade pip
    pip_version=$(pipenv run pip --version)
    echo -e "${GREEN}Pip is installed: $pip_version${NC}"
fi

if [ -d local_lib ]; then
    echo -e "${YELLOW}local_lib exists${NC}"
    rm -rf local_lib
    echo -e "${YELLOW}local_lib is removed${NC}"
else
    echo -e "${BLUE}local_lib does not exist${NC}"
fi

echo -e "${BLUE}Installing path.py from GitHub${NC}"
pipenv run pip install git+https://github.com/jaraco/path.py.git -t local_lib 
echo -e "${GREEN}path.py is installed from GitHub${NC}"

echo -e "${BLUE}Running my_program.py${NC}"
pipenv run python3 my_program.py 2>&1 | tee /dev/tty