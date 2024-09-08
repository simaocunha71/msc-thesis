  let fruits = s.split(' ');
  let apples = parseInt(fruits[0].split(' ')[1]);
  let oranges = parseInt(fruits[1].split(' ')[0]);
  return n - (apples + oranges);
}



