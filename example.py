import os
from memdump import memprint

data = os.urandom(100)
memprint(data)
