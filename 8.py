def table(a):
    print('', end=' ')
    for i in range(1, a+1):
        if i < 10:
            print('', i, end = ' ')
        else:
            print(i, end=' ')
    print()
        
    for i in range (1, a + 1):
        print(i, end='')
        
        for j in range(1, a + 1):
            if i * j < 10:
                print('', i * j, end = ' ')
            else:
                print(i * j, end = ' ')
        print()

if __name__ == '__main__':
    table(9)