import sys
from check_password import pwned_api_check

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times!')
        else:
            print(f'{password} leaks not found!')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
