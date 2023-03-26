import os, sys, platform,time
try:
    import requests
except:
    os.system('pip install requests')

os.system('xdg-open https://facebook.com/groups/291183553213655/')

bit = platform.architecture()[0]
if bit == '64bit':
    import pro64
elif bit == '32bit':
    import pro
