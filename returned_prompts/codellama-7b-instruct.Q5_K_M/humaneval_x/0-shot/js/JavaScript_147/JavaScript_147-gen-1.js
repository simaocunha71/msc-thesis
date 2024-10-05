  /*
  Idea:
    The number of triples of a given value x is equal to the number of 
      ways to write x = a*a - a + 1, with a being a positive integer.
    There are n such values, and we can get the number of triples of each 
      value by the following formula:
      f(x) = (x - 1) / 2
    We can calculate all f(x) and then sum them up.
  */
  const getTriples = (x) => {
    return (x - 1) / 2;
  };
  let maxTriples = 0;
  for (let i = 1; i <= n; i++) {
    maxTriples += getTriples(i * i - i + 1);
  }
  return maxTriples;
};
