import urllib

import urllib3

http = urllib3.PoolManager()
r = urllib.request.urlopen(
    'localhost:8000',
    data= '0\nint,3\nint,3'
)
