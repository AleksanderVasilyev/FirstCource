
s = 'иванов иван'

r=s.split()

print(r)

for i in r:
    if i[0].isalpha()==True:
        print(i[0].upper())
        i[0].replace('и','И')
    print(i, end=' ')