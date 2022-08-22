import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "`~!#@$%^&*()_+=-|][{};:'/?.,><"

comb = lower + upper + numbers + symbol
length = 16

password = "".join(random.sample(comb, length))
print(password)