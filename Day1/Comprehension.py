
def main():
    numbers = [1, 2, 3, 4]

    changed = []
    for value in numbers:
        if value != 3:
            changed.append(value*2)
        else:
            changed.append(value)

    print(changed)

    changed = [value*2 if value != 3 else value for value in numbers]
    print(changed)

    x_and_y = []
    for x in range(2,6,2):
        for y in range(3,7,2):
            if x < y:
                x_and_y.append((x,y))
    print(x_and_y)

    x_and_y = [(x, y) if x < 4 else 'Boom' for x in range(2, 6, 2) for y in range(3, 7, 2) if x < y]
    print(x_and_y)



if __name__ == '__main__':
    main()