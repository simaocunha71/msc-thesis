  var sum = 0;

  for (var i = 0; i < s.length; i++) {
    let char = s[i];
    if (char.toUpperCase() === char) {
      sum += char.charCodeAt(0);
    }
  }

  return sum;
}



