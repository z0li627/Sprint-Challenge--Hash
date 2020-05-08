def get_indices_of_item_weights(weights, length, limit):
    idx = {}
    for i in range(len(weights)):
        if weights[i] not in idx:
            idx[weights[i]] = [i]
        else:
            idx[weights[i]] += [i]
    
    for weight in weights:
        if limit - weight in idx:
            if weight == limit - weight:
                return [idx[weight][1], idx[weight][0]]
            elif weight > idx[limit - weight][0]:
                return [idx[limit - weight][0], idx[weight][0]]
            else:
                return [idx[weight][0], idx[limit - weight][0]]