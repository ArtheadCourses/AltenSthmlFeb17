class A:
    def __init__(self):
        print('Constructor A')

class B(A):
    def __init__(self):
        print("Constructor B")
        super().__init__()

class C(A):
    def __init__(self):
        print("Constructor C")
        super().__init__()

class D(C, B):
    def __init__(self):
        print("Constructor D")
        super().__init__()



def main():
    d = D()
    print(D.__mro__)
    
if __name__ == '__main__':
    main()