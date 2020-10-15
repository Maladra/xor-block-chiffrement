import base64


## Function to xor byte by byte
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


f = open('blackhole.jpg', 'rb')
f_read = f.read() # in byte for b64
f.close

## Convert to b64
b64_encode = base64.b64encode(f_read)
n = 256
xor_key = b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gUGhhc2VsbHVzIHRpbmNpZHVudCwgZHVpIGFjIHJ1dHJ1bSBwcmV0aXVtLCBhbnRlIG1hc3NhIHVsbGFtY29ycGVyIGp1c3RvLCBpZCBhbGlxdWFtIGxhY3VzIG51bmMgZXQgaXBzdW0uIENyYXMgdmVsIHNhcGllbiBpZCBuaXNsIGF1Y3Rv'
chunk_list = [b64_encode[i:i+n] for i in range (0, len(b64_encode), n)]

## Add padding
for item in chunk_list:
    if len(item) < n:
        chunk_list.remove(item)
        while len(item) < n:
            item = item + b'*'
        chunk_list.append(item)

    
xored_array = []

## initial
xored_array.append(byte_xor(chunk_list[0],xor_key))

## xor
i = 1
while i < (len(chunk_list)):
    xored_array.append(byte_xor(chunk_list[i],xored_array[i-1]))
    i = i+1

## Concatenate in bytes
full_bytes = b''
for item in xored_array:
    full_bytes = full_bytes + item


f = open("chiffrer.jpg", 'wb')
f.write(full_bytes)
f.close()
