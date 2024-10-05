    return [abs(guess - game) if guess != game else 0 for guess, game in zip(guess, game)]


