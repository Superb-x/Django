import os

def search(path):
    for x in os.listdir(path):
        file = os.path.join(path, x)
        print(file)
        if os.path.isdir(file):
            search(file)

search('.')