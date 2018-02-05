filename = 'db.txt'


def encwrite():
    db = open(filename,'a')
    db.write(enc('work') + '\n')
    db.write(enc('now')+ '\n')
    db.close()


def enc(str):
    return ' '.join(format(ord(x), 'b') for x in str)


with open(filename, 'rb') as r:
    content = r.read()
    print(content)

encwrite()
