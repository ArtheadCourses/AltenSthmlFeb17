def test_func(x, y):
    try:
        z = x / y
    except ZeroDivisionError as e:
        print(e)

def main():
    x = 10
    y = 0
    test_func(x, y)



if __name__ == '__main__':
    main()