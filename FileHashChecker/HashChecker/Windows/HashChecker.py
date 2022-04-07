import hashlib
import subprocess
import sys



if len(sys.argv) != 2:
    print("[!] Please Enter the Hash File.")
    exit()


def hashed_files():
    hashFILE = open(sys.argv[1], "r").readlines()
    dict = {}
    for i in range(len(hashFILE)):
        hashFILE[i] = hashFILE[i].strip("\n").split(" ")
        dict[hashFILE[i][0]] = hashFILE[i][2]
    return dict





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



def hash_file(filename):

   h = hashlib.sha1()

   with open(filename,'rb') as file:

       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()




files = get_files()

Hashes = hashed_files()

for file in Hashes:
    if file not in files:
        print("[!] " + file + " is missing.")
    else:
        hashed = hash_file(file)
        if hashed == Hashes[file]:
            print("[+] " + file + " : OK.")
        else:
            print("[!] " + file + " : Different Hash Value.")