from sys import argv


def descending(n):
    if n == 1:
        return n
    return (n + descending(n - 1))


def main(argv):
    print descending(int(argv[1]))

if __name__ == '__main__':
    main(argv)
