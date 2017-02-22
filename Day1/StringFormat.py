
def main():
    name = 'Peter'
    age = 34

    s = "Hi {0} you are {1} years old. Bye {0}".format(name, age)
    print(s)
    s2 = f"Hi {name} you are {age} years old. Bye {name}"
    print(s2)


if __name__ == '__main__':
    main()