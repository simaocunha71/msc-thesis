
def compare(game, guess):
    return [abs(g - h) for g, h in zip(game, guess)]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # [4,4,1,0,0,6]
<jupyter_output>
[0, 0, 0, 0, 3, 3]
[4, 4, 1, 0, 0, 6]
<jupyter_text>
Problem 3:
<jupyter_code>
