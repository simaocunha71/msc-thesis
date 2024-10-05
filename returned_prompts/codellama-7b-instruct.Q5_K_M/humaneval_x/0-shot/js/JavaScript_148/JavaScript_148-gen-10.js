const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];

const orbit1 = planets.indexOf(planet1);
const orbit2 = planets.indexOf(planet2);

const result = [];

if (orbit1 === -1 || orbit2 === -1) {
  return [];
}

for (let i = orbit1; i <= orbit2; i++) {
  result.push(planets[i]);
}

return result.sort((a, b) => a - b);
