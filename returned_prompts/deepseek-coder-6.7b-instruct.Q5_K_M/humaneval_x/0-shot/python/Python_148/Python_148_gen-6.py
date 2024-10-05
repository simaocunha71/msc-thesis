
planet_order = ["Mercury", "Venus", "Earth", "Mars", 
                "Jupiter", "Saturn", "Uranus", "Neptune"]

def bf(planet1, planet2):
    if planet1 not in planet_order or planet2 not in planet_order:
        return ()
    else:
        start = planet_order.index(planet1)
        end = planet_order.index(planet2)
        if start > end:
            start, end = end, start
        return tuple(planet_order[start+1:end])

print(bf("Jupiter", "Neptune"))  # ==> “Saturn", "Uranus")
print(bf("Earth", "Mercury"))  # ==> “Venus")
print(bf("Mercury", "Uranus"))  # ==> “Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Pluto", "Neptune"))  # ==> ())
print(bf("Neptune", "Pluto"))  # ==> ())
print(bf("Neptune", "Neptune"))  # ==> ())
print(bf("Mercury", "Mercury"))  # ==> ())
print(bf("Pluto", "Uranus"))  # ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

In the first line, the function is creating a list of planets from closest to the sun to farthest. 

In the second line, it is checking if planet1 or planet2 are not in the list of planets. If either of them are not in the list, it returns an empty tuple. 

In the third line, it finds the index of planet1 and planet2 in the list of planets. It then checks if the index of planet1 is greater than the index of planet2. If it is, it swaps the two indices. 

In the fourth line, it slices the list of planets from the index of planet1 plus one to the index of planet2 and returns this slice as a tuple. The plus one is needed because the function should not include