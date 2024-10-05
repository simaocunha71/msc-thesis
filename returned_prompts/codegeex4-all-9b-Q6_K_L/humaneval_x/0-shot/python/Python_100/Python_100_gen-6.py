def make_a_pile(n):
    stones = [n]
    for i in range(n-1):
        stones.append(stones[-1] + 2*(i%2+1))
    return stones

print(make_a_pile(3))
print(make_a_pile(4))
print(make_a_pile(5))
print(make_a_pile(6))