import my_module
import my_module as mm
from my_module import add
from my_module import add as add2
#from my_module import * Should be avoided

# Overrides the import
def add(a, b):
    return a - b

def main():
    print(my_module.add(3,4)) # Uses import my_module
    print(add(3,2))           # Uses from my_module import add
    print(add2(3,2))          # Uses from my_module import add as add2
    print(mm.add(9,5))        # Uses import my_module as mm
    pass

if __name__ == '__main__':
    main()