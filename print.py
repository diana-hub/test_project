f = open('data.txt', 'r')
data = f.read()
print(data)
data2 = data.decode('utf-8').upper()
print(data2)
