
fo = open('test.txt', 'a')

#get info from file
print('name:', fo.name)
print('is closed', fo.closed)

fo.write(' love python\n')
fo.close()

f = open('test.txt')
buff = f.read(11)
print(buff)
