## Chiffrement
# 1) lire fichier OK
# 2) encoder base64 OK
# 3) decouper base64 en bloc OK 
# 5) char chaque bloc melange
# 4) add padding last bloc OK 
# 6) xorer chaque bloc
# 7) associer resultat
# 8) afficher

import time
import base64


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


f = open('lorem.txt')
f_read = f.read().encode("utf-8") # in byte for b64
f.close
b64_encode = base64.b64encode(f_read)
b64_str = b64_encode.decode('utf-8')

n = 256
xor_key = b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gUGhhc2VsbHVzIHRpbmNpZHVudCwgZHVpIGFjIHJ1dHJ1bSBwcmV0aXVtLCBhbnRlIG1hc3NhIHVsbGFtY29ycGVyIGp1c3RvLCBpZCBhbGlxdWFtIGxhY3VzIG51bmMgZXQgaXBzdW0uIENyYXMgdmVsIHNhcGllbiBpZCBuaXNsIGF1Y3Rv'
chunk_list = [b64_str[i:i+n] for i in range (0, len(b64_str), n)]


for item in chunk_list:
    if len(item) < 128:
        chunk_list.remove(item)
        while len(item) < 128:
            item = item + '*'
        chunk_list.append(item)

    
chunk_list_byte = []
for item in chunk_list:
    chunk_list_byte.append(item.encode('utf-8'))

xored_array = []
for item in chunk_list_byte:
    xored_array.append(byte_xor(item,xor_key))


full_bytes = b''
for item in xored_array:
    full_bytes = full_bytes + item


f = open("chiffrer.txt", 'wb')
f.write(full_bytes)
f.close()
