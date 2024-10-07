def denominator(arr):
    res = []
    for i in range(2, min(arr) + 1):
        for j in range(len(arr)):
            if arr[j] % i != 0:
                break
        else:
            res.append(i)
    return res

if __name__ == '__main__':
    print(denominator([42, 12, 18]))