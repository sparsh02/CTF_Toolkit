import base64
import sys

message = sys.argv[1]

message = message.encode('UTF-8')

print (base64.b32encode(message).decode('UTF-8'))