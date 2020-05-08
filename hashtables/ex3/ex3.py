def intersection(arrays):
    data = {}
    result = []

    for i in arrays:
        for j in i:
            if j not in data:
                data[j] = 1
            else:
                data[j] += 1
    
    for key, val in data.items():
        if len(arrays) <= val:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
