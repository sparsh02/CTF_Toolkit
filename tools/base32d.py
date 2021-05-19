import base64
import sys

message = sys.argv[1]

print (base64.b32decode(message).decode('UTF-8'))