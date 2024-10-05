
def bf(planet1, planet2):
    planet_order = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    else:
        start_index = planet_order.index(planet1)
        end_index = planet_order.index(planet2)
        if start_index < end_index:
            return tuple(planet_order[start_index+1:end_index+1])
        else:
            return tuple(planet_order[start_index+1:]+planet_order[:end_index+1])
