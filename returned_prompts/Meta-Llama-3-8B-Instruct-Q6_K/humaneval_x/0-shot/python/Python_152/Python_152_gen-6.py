def compare(game,guess):
    return [abs(g-s) if g!=s else 0 for g,s in zip(game,guess)]


# test cases
print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) # -> [0,0,0,0,3,3]
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) # -> [4,4,1,0,0,6] 
print(compare([1,2,3,4,5,6],[1,2,3,4,5,7])) # -> [0,0,0,0,0,1]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,4])) # -> [0,0,0,0,0,2]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,3])) # -> [0,0,0,0,0,3]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,8])) # -> [0,0,0,0,0,2]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,9])) # -> [0,0,0,0,0,3]
print(compare([1,2,3,4,5,6],[1,2,3,4,5,10])) # -> [0,0,0,0,0,4]

B:

def compare(game,guess):
    return [abs(g-s) if g!=s else 0 for g,s in zip(game,guess)]

print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]))
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]))
print(compare([1,2,3,4,5,6],[1,2,3,4,5,7]))
print(compare([1,2,3,4,5,6],[1,2,3,4,5,4]))
print(compare