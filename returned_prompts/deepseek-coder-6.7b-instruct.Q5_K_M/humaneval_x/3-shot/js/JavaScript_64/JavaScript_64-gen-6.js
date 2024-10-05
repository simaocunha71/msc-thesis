  var count = 0;
  var stringLower = s.toLowerCase();
  for  (var i = 0; i < stringLower.length; i++) {
    if  (stringLower[i] === 'a' || stringLower[i] === 'e' || stringLower[i] === 'i' || stringLower[i] === 'o' || stringLower[i] === 'u') {
      count++;
    }
  }
  if  (s[s.length - 1] === 'y') {
    count++;
  }
  return count;
}



