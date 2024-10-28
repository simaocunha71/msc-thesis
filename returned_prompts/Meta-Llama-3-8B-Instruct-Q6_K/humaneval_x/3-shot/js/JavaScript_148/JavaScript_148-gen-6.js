  let planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  let index1 = planets.indexOf(planet1);
  let index2 = planets.indexOf(planet2);
  
  if (index1 === -1 || index2 === -1) {
    return ();
  }
  
  let result = [];
  for (let i = index1 + 1; i < index2; i++) {
    result.push(planets[i]);
  }
  
  return (result);
}