import subprocess
import hashlib



def hash_file(filename):

   h = hashlib.sha1()

   with open(filename,'rb') as file:

       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()



def check_file(file):
    exceptions = ["Hashes.txt", "FileHasher.py", "HashChecker.py"]
    if file in exceptions:
        return False
    sub_files = file.split(".")
    if len(sub_files) > 1:
        ext = sub_files[-1]
        if ext.isalpha() or ext=="ps1":
            return True
    return False



def rm_empty_str(l):
    return [word for word in l if word!=""]


def get_files():
    fles  = subprocess.check_output("dir", shell=True).decode().split("\n")
    fles = [file.strip("\r") for file in fles]

    files = []

    for f in fles:
        f = f.split(" ")
        f = rm_empty_str(f)
        file = "".join(f[4:])
        files.append(file)
    return files


files = get_files()


Hashes = open("Hashes.txt", "w")


for file in files:
    if check_file(file):
        Hashes.write(file + " : " + hash_file(file))