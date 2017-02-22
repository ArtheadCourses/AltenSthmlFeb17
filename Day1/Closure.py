# LEGB
#__name__ = 'Hepp'


def outer():
    #__name__ = 'Hopp'
    def inner():
        #__name__ = 'Hi'
        print(__name__)
    inner()

#def func():

#    global x
    #x += 1
#    print(x)


def main():
 #   func()
 #   print(x)

    outer()

if __name__ == '__main__':
    main()

