
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
planet_dict = {'Mercury': 0.31, 'Venus' : 0.724, 'Earth': 1, 'Mars':1.587, 'Jupiter': 5.203, 'Saturn':9.543, 'Uranus':19.2, 'Neptune':30}
def bf(planet1, planet2):  
    if not planet_dict[planet1] <= planet_dict[planet2]:  #Checking if the planet names are correct and in alphabetical order 
        return ()
    elif planet_dict[planet2] > planet_dict[planet1]:#checking to see if the planets are in alphabetic order
        return ()
    else:
        if planet1 == planet2: #Checking for the if statement  
            return ()
        else: 
            if planet1 <= planet_dict[planet2] and planet1 <= planet_dict[planet1]:
                i = planet1 - 1
                j = (planet1 - 1) + planet2-