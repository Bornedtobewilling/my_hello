import sys

def panda():
    print('I love China! ')

def default():
    print('Not a panda')

def main():
    if sys.argv[1] == 'panda':
        panda()
    else:
        default()

if __name__ == '__main__':
    main()
