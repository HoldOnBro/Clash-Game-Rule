import re,os

from numpy import full


def findAllFile(source):
    for root, ds, fs in os.walk(source):
        for f in fs:
                fullname = os.path.join(root, f).replace("\\", "/")
                print(fullname)
                yield fullname

def go(source):
    for file in findAllFile(source):
        # print(file)
        lines = []
        with open(file, 'r+', encoding='utf-8') as f:
            lines = f.readlines()
        with open(file, 'w+', encoding='utf-8') as f:
            for i in range(1,len(lines)):
                lines[i] = "  - " + lines[i]
            f.writelines(lines)
        with open(file, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('payload:\n'+content)
        with open(file, 'a', encoding='utf-8') as f:
            f.write("\n")

def main():
    go("D:/GitHub Desktop/Clash-Game-Rule/rules")
main()