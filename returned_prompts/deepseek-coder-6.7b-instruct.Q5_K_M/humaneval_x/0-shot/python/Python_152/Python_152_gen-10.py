
def compare(game, guess):
    result = []
    for i in range(len(game)):
        result.append(abs(game[i] - guess[i]))
    return result

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]))
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]))
<jupyter_output>
[0, 0, 0, 0, 3, 3]
[4, 4, 1, 0, 0, 6]
<jupyter_text>
