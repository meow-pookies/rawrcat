# rawrcat v1.0
# 'main.py' -> primary runtime logic and initial execution call -> v1.0
# python version 3.13.5
# dependencies:
#  global -> 'os' 'rsa' 'pycrypto' 'pycryptodome' 'colorama' 'platform'
#  local-packages -> 'iomgr' 'pkcs1_oaep'
#  self -> 'os' 'platform'
# [!] some local packages require dependencies that are obsolete and have been deprecated
# [!] undefined exception handling rules

# import dependencies
import os, platform

# import local packages
from lib import pkcs1_oaep as cryptography
from lib.iomgr import iostream as xcnsl
from lib.iomgr import shell as xcnslfunc

########  < INIT >  ########

# clear command line and display splash
xcnslfunc.clear()
xcnsl.log('\n\ninitializing...', 3, "\n                       _,-'""`-._        \n  rawrcat v1.0    |`._,'(       |\\`-/|   \n                   `-.-' \\ )-`( , o o)   \n                        ^^^^^^^^^^^^^^   ")

# define global variables 
OSTYPE = str(platform.system().lower())
CWD = os.getcwd()
xcnsl.log(str('detected ostype \'' + str(OSTYPE) + '\''))
xcnsl.log(str('cwd = \'' + str(CWD) + '\''))
