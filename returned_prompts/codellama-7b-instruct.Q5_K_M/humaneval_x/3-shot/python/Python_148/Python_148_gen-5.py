    if planet1 not in {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}:
        return ()
    if planet2 not in {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}:
        return ()
    if planet1 == planet2:
        return ()
    if planet1 == "Mercury":
        if planet2 == "Neptune":
            return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    if planet2 == "Mercury":
        if planet1 == "Neptune":
            return ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
        return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    if planet1 == "Earth":
        if planet2 == "Neptune":
            return ("Venus", "Mars", "Jupiter", "Saturn", "Uranus")
        return ("Venus", "Mars", "Jupiter", "Saturn")
    if planet2 == "Earth":
        if planet1 == "Neptune":
            return ("Venus", "Mars", "Jupiter", "Saturn", "Uranus")
        return ("Venus", "Mars", "Jupiter", "Saturn")
    if planet1 == "Mars":
        if planet2 == "Neptune":
            return ("Jupiter", "Saturn", "Uranus")
        return ("Jupiter", "Saturn")
    if planet2 == "Mars":
        if planet1 == "Neptune":
            return ("Jupiter", "Saturn", "Uranus")
        return ("Jupiter", "Sat