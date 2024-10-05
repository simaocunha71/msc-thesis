    return [abs(game[i]-guess[i]) if game[i] != guess[i] else 0 for i in range(len(game))]
    # This function compares each score with its corresponding guess, and returns an array of the differences.
    # If the guess is correct (i.e., the score and guess are equal), it returns 0. If not, it returns the absolute difference between the score and the guess. 
    # This is done for each match in the game and guess arrays.