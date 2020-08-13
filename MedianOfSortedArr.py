def MedianOfSortedArray(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1


    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1

    print(c)
    print(len(c))

    q, r = divmod(len(c), 2)
    if r == 0:
        print('c[q]-{} c[q-1]-{} Median- {}'.format(c[q], c[q-1], (c[q] + c[q - 1]) / 2))
    else:
        print('c[q] and Median -{}'.format(c[q]))


a = [1,2]
b = [3,5]
MedianOfSortedArray(a, b)
