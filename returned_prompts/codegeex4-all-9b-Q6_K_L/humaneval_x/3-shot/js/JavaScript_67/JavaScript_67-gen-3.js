  var apples = parseInt(s.split('apples')[0]);
  var oranges = parseInt(s.split('oranges')[0].split('apples')[1]);
  return n - apples - oranges;
}



