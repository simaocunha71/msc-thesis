    sentences = S.split('. ')  # Split the string into sentences
    boredoms = [s for s in sentences if s and s.startswith('I')]  # Filter sentences that start with 'I'
    return len(boredoms)  # Return the number of boredoms


