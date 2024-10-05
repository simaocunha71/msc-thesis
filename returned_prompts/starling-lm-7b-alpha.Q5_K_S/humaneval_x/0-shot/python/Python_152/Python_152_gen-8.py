
def compare(game,guess):
    res = []
    for i in range(len(game)):
        res.append(abs(game[i]-guess[i]))
    return res


# Other solutions:
# def compare(game,guess):
#     return [abs(game[i] - guess[i]) for i in range(len(game))]

# def compare(game, guess):
#     return [abs(game[i] - guess[i]) for i in xrange(len(game))]


# def compare(game,guess):
#     return [abs(game[i]-guess[i]) for i in range(len(game))]

# def compare(game,guess):
#     return [abs(game[i] - guess[i]) for i in range(len(game))]

# def compare(game,guess):
#     return [abs(game[i]-guess[i]) for i in range(len(game))]

# def compare(game,guess):
#     return [abs(game[i] - guess[i]) for i in xrange(len(game))]

# def compare(game,guess):
#     return [abs(game[i] - guess[i]) for i in xrange(len(game))]

# def compare(game,guess):
#     return [abs(game[i] - guess[i]) for i in range(len(game))]

# def compare(game,guess):
#     return [abs(game[i] - guess[i]) for i in range(len(game))]
```