import sys

file_db = open('db.txt', 'a+')

first_arg = sys.argv[1]
second_arg = sys.argv[2]


def write_to(key=first_arg, val=second_arg):
    file_db.write("{} {}".format(key, val))
    pair = "%s:%s" % (key, val)
    f = file_db
    print(pair)
    f.write(enc(pair) + '\n')
    f.close()


with open('db.txt', "rb") as binary_file:
    data = binary_file.read()
    print(data)


def enc(string):
    return "".join([format(ord(char), '#010b')[2:] for char in string])


if __name__ == "__main__":
    write_to()
