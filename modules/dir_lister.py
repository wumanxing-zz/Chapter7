import os


def run(**kwargs):

    print "[*] In dir lister module"

    files = os.listdir(".")

    return str(files)

