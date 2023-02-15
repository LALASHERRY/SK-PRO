try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from SK64 import main

    main() 

elif bit == '32bit':

    from SK32 import main

    main()
