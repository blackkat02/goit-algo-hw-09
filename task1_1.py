def find_coins_greedy(nums: list[int], amount: int):
    coins_dict = {}
    for coin in sorted(nums, reverse=True):
        if coin <= amount:
            k = amount // coin
            amount -= k * coin
            coins_dict[coin] = k

    return coins_dict


list_nums = [50, 25, 10, 5, 2, 1]
list_nums2 = [10, 6, 3, 1]


print(find_coins_greedy(list_nums,113))
print(find_coins_greedy(list_nums,93))
print(find_coins_greedy(list_nums,143))
print(find_coins_greedy(list_nums,91))
print(find_coins_greedy(list_nums,43))
print(find_coins_greedy(list_nums,1358))
print(find_coins_greedy(list_nums2, 12))
print(find_coins_greedy(list_nums2, 15))
print(find_coins_greedy(list_nums2,1358))






