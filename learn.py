from config.config import index , password
from rich import print as printc
import hashlib
import sys

pw = password()
hashed =hashlib.sha256(pw.encode()).hexdigest()

print(hashed)
print(len(hashed))
print("!" * 4)
print(sys.argv[2])

