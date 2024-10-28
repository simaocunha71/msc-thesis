def compare(game, guess):
    return [abs(game[i]-guess[i]) for i in range(len(game))]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]))
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]))