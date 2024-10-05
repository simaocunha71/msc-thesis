  var count = 0;
  for (var i = 0; i < string.length; i++) {
    var char = string[i];
    var lowerChar = char.toLowerCase();
    if (string.indexOf(lowerChar) == i) {
      count++;
    }
  }
  return count;
}



