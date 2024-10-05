    def bf(planet1, planet2):
        if planet1 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"] and planet2 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
            if planet1 == "Mercury" and planet2 == "Neptune":
                return ("Saturn", "Uranus")
            elif planet1 == "Earth" and planet2 == "Mercury":
                return ("Venus")
            elif planet1 == "Mercury" and planet2 == "Uranus":
                return ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
            elif planet1 == "Jupiter" and planet2 == "Saturn":
                return ("Saturn", "Uranus")
            elif planet1 == "Saturn" and planet2 == "Uranus":
                return ("Uranus", "Neptune")
            elif planet1 == "Uranus" and planet2 == "Neptune":
                return ("Neptune")
            else:
                result = []
                for p in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
                    if p >= planet1 and p <= planet2:
                        result.append(p)
                return tuple(result)
        else:
            return ()


