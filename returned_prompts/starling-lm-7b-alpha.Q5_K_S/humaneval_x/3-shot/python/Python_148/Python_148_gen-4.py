    def bf(planet1, planet2):
        planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
        if planet1 not in planets or planet2 not in planets:
            return ()

        if planet1 > planet2:
            planet1, planet2 = planet2, planet1

        result = ()
        for planet in planets:
            if planet1 == planet:
                continue

            if planet == planet2:
                return result

            result = result + (planet,)

        return result


