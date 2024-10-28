  const planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Jupiter',
  'Saturn',
  'Uranus',
  'Neptune'
  ];

  const index1 = planets.indexOf(planet1);
  const index2 = planets.indexOf(planet2);

  if  (index1  != -1  && index2  != -1)  {
    return planets.slice(Math.min(index1, index2) + 1, Math.max(index1, index2));
  }  else  {
    return ();
  }
}



