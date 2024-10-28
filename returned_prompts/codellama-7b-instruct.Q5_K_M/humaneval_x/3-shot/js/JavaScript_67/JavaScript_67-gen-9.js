  var apples = 0;
  var oranges = 0;

  s = s.split(' ');
  if (s[0] == '0') {
    apples = 0;
  } else {
    apples = parseInt(s[0]);
  }

  if (s[2] == '0') {
    oranges = 0;
  } else {
    oranges = parseInt(s[2]);
  }

  return n - apples - oranges;
}



