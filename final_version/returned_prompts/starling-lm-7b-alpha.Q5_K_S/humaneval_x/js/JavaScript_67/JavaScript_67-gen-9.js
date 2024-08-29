  let apples = s.match(/\d+ apples/g);
  let oranges = s.match(/\d+ oranges/g);
  let mangos = n - apples.length - oranges.length;
  return mangos;
}



