import base64

## Function to xor byte by byte
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

xor_key = b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gUGhhc2VsbHVzIHRpbmNpZHVudCwgZHVpIGFjIHJ1dHJ1bSBwcmV0aXVtLCBhbnRlIG1hc3NhIHVsbGFtY29ycGVyIGp1c3RvLCBpZCBhbGlxdWFtIGxhY3VzIG51bmMgZXQgaXBzdW0uIENyYXMgdmVsIHNhcGllbiBpZCBuaXNsIGF1Y3Rv'


f = open('chiffrer.jpg', 'rb')
f_read = f.read()
f.close()

# Lenth bloks and key
n = 256
# chunk array
xored_chunk_list = [f_read[i:i+n] for i in range (0, len(f_read), n)]

## end of chunk array
i = len(xored_chunk_list) -1
byte_chunk_array = []

## CBC revert
while i >= 0:
    if i == 0:
        byte_chunk_array.append(byte_xor(xored_chunk_list[i], xor_key))
        break
    byte_chunk_array.append(byte_xor(xored_chunk_list[i], xored_chunk_list[i-1]))
    i = i-1

#reverse list
byte_chunk_array.reverse()

final_bytes = b''
for item in byte_chunk_array:
    final_bytes = final_bytes + item

## Remove padding
stiped_final = final_bytes.rstrip(b'*')

b64_decode = base64.b64decode(stiped_final)
## Write result
f = open("clear_final", 'wb')
f.write(b64_decode)
f.close()