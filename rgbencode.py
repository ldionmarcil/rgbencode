import Image
import sys
path = './foo.png'
f=sys.argv[1]
o=[[]]

for i, j in enumerate(f):
    o[-1].append(ord(j))
    if (i+1) % 3 == 0 and (i+1) != len(f):
        o.append([])
        
while (3- len(o[-1])) > 0:
    o[-1].append(0)

img = Image.new('RGB', (len(o),1))
for i,j in enumerate(o):
    img.putpixel((i,0), (j[0], j[1], j[2]))
img.save(path)

img = Image.open(path)
x,y=img.size
o=''

def chrCast(x):
    if x:
        return chr(x)
    else:
        return ''
for i in range(x):
    o = '%s%s' % (o, (''.join([chrCast(x) for x in img.getpixel((i,0))])))
print o
