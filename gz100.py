import sys, gzip
print('LOG')
try:
    times = int(sys.argv[4])
except (IndexError, ValueError):
    times = 100
print('LOG')
try:
    f = open(sys.argv[3], 'rb')
except (PermissionError, OSError, FileNotFoundError, IndexError): sys.exit()
print('LOG')
content = f.read()
print('LOG')
f.close()
print('LOG')
t = sys.argv[1]
print('LOG')
if t=='COMPRESS': func=gzip.compress
elif t=='DECOMPRESS': func=gzip.decompress
else: sys.exit()
print('LOG')
for i in range(times): content = func(content)
print('LOG')
try:
    f = open(sys.argv[2], 'wb')
except (PermissionError, OSError, FileNotFoundError):
    sys.exit()
print('LOG')
f.write(content)
print('LOG')
f.close()
