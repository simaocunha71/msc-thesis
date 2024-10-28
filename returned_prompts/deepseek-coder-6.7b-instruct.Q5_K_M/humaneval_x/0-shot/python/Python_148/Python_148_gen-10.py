
def bf(planet1, planet2):
    planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        start = planets.index(planet1)
        end = planets.index(planet2)
        if start > end:
            start, end = end, start
        return planets[start+1:end]

print(bf("Jupiter", "Neptune"))  # ==> 출력: ("Saturn", "Uranus")
print(bf("Earth", "Mercury"))  # ==> 출력: ("Venus")
print(bf("Mercury", "Uranus"))  # ==> 출력: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

'''
주어진 행성들의 순서를 튜플에 저장하고 있습니다. 정확한 행성 이름이 아닐 경우 빈 튜플을 반환합니다. 
만약 주어진 행성들의 순서가 올바르지 않은 경우, 순서를 바꿔서 반환합니다. 
그리고 그 사이에 있는