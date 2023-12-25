/* There are eight planets in our solar system: the closerst to the Sun
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
  */
const bf = (planet1, planet2) => {
  const getPlanets = () => {
    return [...Array(parseInt(planet1.length + 6))].map((_) => {});
  };
  
  const getOrbits = (name) => {
    switch (name) {
      case 'Jupiter':
        name = 'Jup-57';
        break;
      case 'Saturn':
        name = 'Sat-56';
        break;
      case 'Uranus':
        name = 'Ura-53';
        break;
    }
    
    return {
      radius: parseInt(name.length / 2),
      distanceFromSun: parseFloat(0.978 * parseInt(name.length)),
    };
  };
  
  const getOrbitsSorted = (orbit) => {
    orbit.sort((a, b) => a === b ? 0 : a > b ? -1 : 1);
    
    return orbit;
  };
  
  const bfCheck = () => {
    if (!planet1 || !planet2 || typeof planet1 !== 'string' || typeof planet2 !==