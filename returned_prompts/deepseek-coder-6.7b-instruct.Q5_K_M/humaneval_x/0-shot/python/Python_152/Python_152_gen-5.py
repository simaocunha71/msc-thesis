
def compare(game, guess):
    result = []
    for i in range(len(game)):
        result.append(abs(game[i] - guess[i]))
    return result

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # [4,4,1,0,0,6]

# OR

def compare(game, guess):
    return [abs(g - h) for g, h in zip(game, guess)]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # [4,4,1,0,0,6]

# OR

def compare(game, guess):
    return list(map(abs, [game[i] - guess[i] for i in range(len(game))]))

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # [4,4,1,0,0,6]

# OR

def compare(game, guess):
    return [abs(a-b) for a, b in zip(game, guess)]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # [4,4,1,0,0,6]