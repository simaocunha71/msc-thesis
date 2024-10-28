def max_aggregate(lst):
    # Create a dictionary to store the names and their aggregate scores
    scores = {}
    
    # Iterate over the list of tuples
    for name, score in lst:
        # If the name is already in the dictionary, add the score to the existing score
        if name in scores:
            scores[name] += score
        # Otherwise, add the name and score to the dictionary
        else:
            scores[name] = score
    
    # Find the name with the maximum aggregate score
    max_name = max(scores, key=scores.get)
    
    # Return the name and the maximum aggregate score
    return (max_name, scores[max_name])