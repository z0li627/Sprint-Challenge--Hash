def has_negatives(a):
    data = {}
    result = []
    for i in a:
        if i < 0:
            i = i * -1
            data[i] = 0
    
    for j in a:
        if j in data:
            result.append(j)

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
