  var prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];
  var count = 0;
  for (var i = 0; i < num.length; i++) {
    for (var j = 0; j < prime.length; j++) {
      if (prime[j] == num.charCodeAt(i)) {
        count += 1;
      }
    }
  }
  return count;
}



