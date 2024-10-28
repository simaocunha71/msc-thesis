
def compare(game,guess):
    result = []
    for i in range(len(game)):
        result.append(abs(game[i] - guess[i]))
    return result

# Alternative method
def compare(game,guess):
    return [abs(game[i] - guess[i]) for i in range(len(game))]

# Alternative method
from itertools import starmap
from operator import __
def compare(game,guess):
    return list(starmap(__,zip(game,guess)))

# Alternative method
def compare(game,guess):
    return map(lambda x,y:abs(x-y),game,guess)

# Alternative method
def compare(game,guess):
    return map(__, game, guess)

# Alternative method
def compare(game,guess):
    return [abs(game[i] - guess[i]) for i in range(len(game))]

# Alternative method
def compare(game,guess):
    return [abs(game[i] - guess[i]) for i in range(len(game))]

# Alternative method
def compare(game,guess):
    return [abs(game[i] - guess[i]) for i in range(len(game))]

# Alternative method
def compare(game,guess):
    return [abs(game[i] - guess[i]) for i in range(len(game))]

# Alternative method
def compare(game,guess):
    return [abs(game[i] - guess[i]) for i in range(len(game))]

# Alternative method
def compare(game,guess):
    return [abs(game[i] - guess[i]) for i in range(len(game))]

# Alternative method
def compare(game,guess):
    return [abs(game[i] - guess[i]) for i in range(len(game))]

# Alternative method
def compare(game,guess):
    return [abs(game[i] - guess[i]) for i in range(len(game))]