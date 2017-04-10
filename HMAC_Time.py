import timeit
from hashlib import sha1
import hmac

key = "SECRET_KEY"
message = "message"

hashed = hmac.new(key, message, sha1)

start_time = timeit.default_timer()
hmac_digest = hashed.digest()#.encode("base64").rstrip('\n')
elapsed = timeit.default_timer() - start_time

print "=====Without Base64 Encoded====="
print "HMAC Calculation Time = " + str(elapsed) + " sec"
print "Message = " + message
print "Key = " + key
print "Calculated HMAC : " + str(hmac_digest)

