# 
# ## Dechiffrement
# 1) decouper chaque bloc
# 2) xorer chaque bloc avec la clé
# 3) char chaque bloc bon ordre (hormis last)
# 4) assembler bloc
# 5) remove 0 last bloc
# 6) decode base64
# 7) afficher 

import base64

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

xor_key = b'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gUGhhc2VsbHVzIHRpbmNpZHVudCwgZHVpIGFjIHJ1dHJ1bSBwcmV0aXVtLCBhbnRlIG1hc3NhIHVsbGFtY29ycGVyIGp1c3RvLCBpZCBhbGlxdWFtIGxhY3VzIG51bmMgZXQgaXBzdW0uIENyYXMgdmVsIHNhcGllbiBpZCBuaXNsIGF1Y3Rv'


f = open('chiffrer.txt', 'rb')

f_read = f.read()

n = 256
xored_chunk_list = [f_read[i:i+n] for i in range (0, len(f_read), n)]

byte_chunk_array = []
for item in xored_chunk_list:
    byte_chunk_array.append(byte_xor(item,xor_key))


str_chunk_array = []
for item in byte_chunk_array:
    str_chunk_array.append(item.decode('utf-8'))

b64_encode = ''
for item in str_chunk_array:
    b64_encode = b64_encode + item

pading_removed =  b64_encode.replace('*', '')
b64_decode = base64.b64decode(pading_removed)
print (b64_decode.decode('utf-8'))