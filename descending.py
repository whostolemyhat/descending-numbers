from sys import argv


def descending(n):
    """Adds together numbers from n to 0"""
    try:
        n = int(n)
        if n == 1:
            return n
        return (n + descending(n - 1))
    except ValueError:
        print "Couldn't convert to integer"


def main(argv):
    try:
        print descending(int(argv[1]))
    except ValueError:
        print "Couldn't convert to integer"

if __name__ == '__main__':
    main(argv)
