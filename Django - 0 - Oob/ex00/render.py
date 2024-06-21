import sys
import os
import re

def rreplace(s, old, new):
    position = s.rfind(old)
    if position != -1:
        return s[:position] + new + s[position + len(old):]
    else:
        return s

def main():

    try:
        if len(sys.argv) == 2:
            if sys.argv[1].endswith(".template"):
                with open(sys.argv[1], 'r') as file:
                    content = file.read()
                with open("settings.py", 'r') as file1:
                    content1 = file1.read().split('\n')
                    list = {}
                    for i in range(len(content1)):
                        position = content1[i].find("=")
                        position1 = content1[i].find("\"")
                        if position1 and position != -1:
                            name = content1[i][:position]
                            value = content1[i][position1:]
                            list[name] = value.strip("\"")
                for name, value in list.items():
                    content = content.replace('{' + name.strip() + '}', value)
                html = rreplace(sys.argv[1], ".template", ".html")
                with open(html, 'w') as wri:
                    wri.write(content)
    except Exception as e:
        print("Error catch -> " + str(e))

if __name__ == '__main__':
    main()