  const planets_order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

  let planet1_index = planets_order.indexOf(planet1);
  let planet2_index = planets_order.indexOf(planet2);

  if  (planet1_index  == -1  ||  planet2_index  == -1)  {
    return  ()
  }

  return planets_order.slice(Math.min(planet1_index, planet2_index) + 1, Math.max(planet1_index, planet2_index));
}



