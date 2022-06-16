def numDuplicates(name: [], price: [], weight: []) -> int:
    items = list()

    for i in range(len(name)):
        items.append((name[i], price[i], weight[i]))

    uniques = set(items)
    duplicates = len(name) - len(uniques)

    return duplicates


names = ['ball', 'bat', 'glove', 'glove', 'glove', 'ball', 'ball', 'glove']
prices = [2, 3, 1, 1, 2, 2, 2, 1]
weights = [1, 1, 1, 1, 1, 1, 1, 1]

print(numDuplicates(names, prices, weights))
