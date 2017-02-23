from functools import reduce


def myreduce(f, iterable):
    r =  f(a,b)

    r = f(r, a)

def func(a, b):
    if a < b:
        return a
    else:
        return b

def main():
    numbers = [1,22,3,4]
    result = reduce(func, numbers)
    print(result)
 
    

if __name__ == '__main__':
    main()