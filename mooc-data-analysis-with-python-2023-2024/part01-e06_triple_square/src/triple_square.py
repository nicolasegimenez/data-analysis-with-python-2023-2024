#!/usr/bin/env python3
def triple(a):
    return a*3
def square(a):
    return a**2

def main():
    pass
    for i in range(1,11):
        triple_var = triple(i)
        square_var = square(i)
        if square_var > triple_var:
         break
        print(f'triple({i})=={triple_var} square({i})=={square_var}')

if __name__ == "__main__":
    main()
