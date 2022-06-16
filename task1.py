def getMaximumOutfits(outfits: [], money: int) -> int:
    max_length = 0
    for i in range(len(outfits)):
        temp_sum = 0

        for j in range(i, len(outfits)):
            if temp_sum < money:
                temp_sum += outfits[j]
                max_length = max(max_length, ((j - i) + 1))

    return max_length


print(getMaximumOutfits([2, 3, 1, 4, 1, 1, 2, 1], 5))
