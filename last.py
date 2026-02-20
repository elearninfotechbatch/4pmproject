f=open('abc.py','w+')
f.write('hihello')

f.seek(2)

data=f.read(2)
print(data)

f.close()
