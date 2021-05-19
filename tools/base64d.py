import pybase64
import sys


base64_message = sys.argv[1]
base64_bytes = base64_message.encode('ascii')
message_bytes = pybase64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)