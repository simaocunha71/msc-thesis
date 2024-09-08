  let apples = s.match(/apples/gi);
  let oranges = s.match(/oranges/gi);
  let mangoes = n - (apples.length * 1) - (oranges.length * 1);
  return mangoes;
}



