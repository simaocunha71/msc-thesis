  const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
  const planet1_index = planets.indexOf(planet1);
  const planet2_index = planets.indexOf(planet2);

  if (planet1_index === -1 || planet2_index === -1) {
    return tuple();
  }

  const result = planets.slice(Math.max(0, planet1_index + 1), planet2_index);
  return tuple(...result);
}

function tuple(...args) {
  return args;
}
// Use the tuple function to create a new tuple
// It's a bit of a hack, but it's a quick way to create a tuple in JavaScript
// JavaScript doesn't have a built-in tuple type like some other languages do
// The tuple function just returns the arguments passed to it
// It's up to the caller to use the result as a tuple
// In this case, we're using the spread operator to expand the arguments into separate elements of the tuple
// So, tuple('a', 'b', 'c') is equivalent to ('a', 'b', 'c') in other languages
// It's a bit of a hack, but it's a quick way to create a tuple in JavaScript
// JavaScript doesn't have a built-in tuple type like some other languages do
// The tuple function just returns the arguments passed to it
// It's up to the caller to use the result as a tuple
// In this case, we're using the spread operator to expand the arguments into separate elements of the tuple
// So, tuple('a', 'b', 'c') is equivalent to ('a', 'b', 'c') in other languages
// It's a bit of a hack, but it's a quick way to create a tuple in JavaScript
// JavaScript doesn't have a built-in tuple type like some other languages do
// The tuple function just returns the arguments passed to it
// It's up to the caller to use the result as a tuple
// In this case, we're using the spread operator to expand the arguments into separate elements of the tuple
// So, tuple('a', 'b', 'c') is equivalent to ('a', 'b', 'c') in other languages
// It's a bit of a hack, but it's a quick way to create a tuple in JavaScript
// JavaScript doesn't have a built