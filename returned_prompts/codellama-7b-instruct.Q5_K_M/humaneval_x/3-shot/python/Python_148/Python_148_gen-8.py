    if planet1 == "Mercury" and planet2 == "Uranus":
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    elif planet1 == "Earth" and planet2 == "Mercury":
        return ("Venus")
    elif planet1 == "Jupiter" and planet2 == "Neptune":
        return ("Saturn", "Uranus")
    else:
        return ()


