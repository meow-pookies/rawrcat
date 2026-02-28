# rawrcat v1.0
# 'main.py' -> primary runtime logic and initial execution call -> v1.6
# python version 3.13.5
# dependencies:
#  global -> 'os' 'rsa' 'pycrypto' 'pycryptodome' 'colorama' 'platform' 'pathlib' 'uuid'
#  local-packages -> 'iomgr' 'pkcs1_oaep'
#  self -> 'os' 'platform' 'uuid'
# [!] some local packages require dependencies that are obsolete and have been deprecated
# [!] undefined exception handling rules

# import dependencies
import os, platform, uuid

# import local packages
from lib import pkcs1_oaep as cryptography
from lib.iomgr import iostream as xcnsl
from lib.iomgr import shell as xcnslfunc

########  < INIT >  ########

# clear command line and display splash text
xcnslfunc.clear()
xcnsl.log('\n\ninitializing...', 3, "\n\n\n                       _,-'""`-._        \n  rawrcat v1.0    |`._,'(       |\\`-/|   \n                   `-.-' \\ )-`( , o o)   \n                        ^^^^^^^^^^^^^^   ")

# initialization script 
ostype = str(platform.system().lower())
xcnsl.log(str('ostype = \'' + str(ostype) + '\''))

# attempt to locate *.pem keyfiles
if cryptography.keyman.scandir(os.getcwd()) == False:
    xcnsl.log('no keys were found in the active directory\n ..> ' + str(os.getcwd()))
    next = xcnsl.update('set key file target directory or press <enter> to create a new rsa key pair')
    if next == True:
        xcnsl.log('', 5, 'creating new keys:')
        publickey_path = xcnsl.input('set public key target')
        privatekey_path = xcnsl.input('set private key target')
        cryptography.keyman.newkey(publickey_path, privatekey_path, uuid.uuid4().hex, uuid.uuid4().hex)
    else:
        if os.path.exists(next):
            if cryptography.keyman.scandir(next) == False:
                pass
# requires loop