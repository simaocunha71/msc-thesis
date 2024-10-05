def compare(game,guess):
    return [abs(i-j) for i, j in zip(game,guess)]