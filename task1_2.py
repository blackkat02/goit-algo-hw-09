def find_min_coins(nums: list[int], amount: int) -> dict:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coins_used = [0] * (amount + 1)

    for coin in nums:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coins_used[i] = coin

    if dp[amount] == float('inf'):
        return {}

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coins_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result


list_nums = [50, 25, 10, 5, 2, 1]
list_nums2 = [10, 6, 3, 1]


print(find_min_coins(list_nums,113))
print(find_min_coins(list_nums,93))
print(find_min_coins(list_nums,143))
print(find_min_coins(list_nums,91))
print(find_min_coins(list_nums,43))
print(find_min_coins(list_nums,1358))
print(find_min_coins(list_nums2, 12))
print(find_min_coins(list_nums2, 15))
print(find_min_coins(list_nums2,1358))


