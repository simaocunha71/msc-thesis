    return [abs(score-guess) if score!=guess else 0 for score,guess in zip(game,guess)]


