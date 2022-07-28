import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from shazi import ahmad
    ahmad()
elif bit == '32bit':
    from shazi import ahmad
    ahmad()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.sys.exit()
