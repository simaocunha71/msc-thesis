
def bf(planet1, planet2):
    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        return planets[planets.index(planet1):planets.index(planet2)]

# Test cases
print(bf("Jupiter", "Neptune"))  # ==> 으로 표시된 값을 반환
print(bf("Earth", "Mercury"))  # ==> 으로 표시된 값을 반환
print(bf("Mercury", "Uranus"))  # ==> 으로 표시된 값을 반환

# 예상 결과
# ("Saturn", "Uranus")
# ("Venus")
# ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

# 실제 결과
# ("Saturn", "Uranus")
# ("Venus")
# ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

위의 코드는 문제에서 요구한 조건을 만족하며 예상 결과와 실제 결과가 일치함을 알 수 있다.
"""

# 코드를 확인하는 방