f1 = open('o.txt')
f2 = open('p.txt')
a = f1.read()
b = f2.read()
if a == b:
    print 1
else:
    print 0
