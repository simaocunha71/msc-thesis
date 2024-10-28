    eaten = number + min(need - number, remaining)
    return [eaten, remaining - (eaten - number)]


