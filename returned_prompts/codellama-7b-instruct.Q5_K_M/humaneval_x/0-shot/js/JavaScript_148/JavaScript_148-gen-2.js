const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

const planet1Index = planets.indexOf(planet1);
const planet2Index = planets.indexOf(planet2);

if(planet1Index === -1 || planet2Index === -1) {
  return [];
}

const start = Math.min(planet1Index, planet2Index);
const end = Math.max(planet1Index, planet2Index);

return planets.slice(start, end + 1);

