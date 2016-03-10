# Write a function that, given:
#  1. an amount of money
#  2. a list of coin denominations
# computes the number of ways to make amount of money with coins of the available denominations.

class Change:

    def __init__(self):
        self.memo = {}

    def make_change(self, amount, coin_list):
        memo_key = str((amount, coin_list))
        if memo_key in self.memo:
            print "grabbing memo[%s]" % memo_key
            return self.memo[memo_key]

        if amount == 0:
            return 1

        if amount < 0:
            return 0

        if len(coin_list) == 0:
            return 0

        print "checking ways to make %i with %s" % (amount, coin_list)

        current_coin, coins = coin_list[0], coin_list[1:]

        possibilities = 0

        while amount >= 0:
            possibilities += self.make_change(amount, coins)
            amount -= current_coin

        self.memo[memo_key] = possibilities

        return possibilities

change = Change()
print change.make_change(5, [1,2,3])





