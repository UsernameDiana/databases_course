import sys

file_db = open('db.txt', 'a+')

first_arg = sys.argv[1]
second_arg = sys.argv[2]


def write_to(word1=first_arg, word2=second_arg):
    file_db.write("{} {}".format(word1, word2))


with open('db.txt', "rb") as binary_file:
    data = binary_file.read()
    print(data)


if __name__ == "__main__":
    write_to()
