s = 'Café'
len(s)
# 4
b = s.encode('utf8')
# b'Caf\xc3\xa9'
# é is encoded in two bytes
len(b)
# 5

print(b.decode('utf-8'))
# Café