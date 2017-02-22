

def test(name, name_list=None):
    if name_list is None:
        name_list = []
    name_list.append(name)
    return name_list


def main():
    my_list = []
    test('Anna', my_list)
    print(my_list)
    new_list = test('John')
    print(new_list)
    new_list2 = test('Sara')
    print(new_list2)

if __name__ == '__main__':
    main()