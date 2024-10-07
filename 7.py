def prime_numbers(a, b):
    res = []
    for i in range(a, b + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)
    return res

if __name__ == '__main__':
    print(prime_numbers(11, 40))