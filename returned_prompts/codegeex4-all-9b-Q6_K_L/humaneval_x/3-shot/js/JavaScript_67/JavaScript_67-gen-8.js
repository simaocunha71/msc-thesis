  let result = 0;
  let apples = 0;
  let oranges = 0;

  if (s.includes("apples")) {
    apples = parseInt(s.split("apples")[0]);
  }

  if (s.includes("oranges")) {
    oranges = parseInt(s.split("oranges")[0]);
  }

  result = n - apples - oranges;

  return result;
}