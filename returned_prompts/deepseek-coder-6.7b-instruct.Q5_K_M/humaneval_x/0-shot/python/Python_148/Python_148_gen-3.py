
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 in planets and planet2 in planets:
        start = planets.index(planet1)
        end = planets.index(planet2)
        if start > end:
            start, end = end, start
        return tuple(planets[start+1:end])
    else:
        return ()

print(bf("Jupiter", "Neptune"))  #==> ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))  #==> ("Venus")
print(bf("Mercury", "Uranus"))  #==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Mars", "Earth"))  #==> ("Mercury",)
print(bf("Uranus", "Mercury"))  #==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Pluto", "Neptune"))  #==> ()
<jupyter_output>
('Saturn', 'Uranus')
('Venus',)
('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
('Mercury',)
('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
()
<jupyter_text>
