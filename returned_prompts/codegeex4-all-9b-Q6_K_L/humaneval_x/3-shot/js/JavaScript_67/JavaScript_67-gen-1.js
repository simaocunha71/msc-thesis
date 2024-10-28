  let apples = parseInt(s.split('apples')[0]);
  let oranges = parseInt(s.split('oranges')[0].split('and')[1]);
  return n - apples - oranges;
}