  var seen = {};

  for (var i = 0; i < string.length; i++) {
    var c = string[i];
    if (seen[c.toLowerCase()]) {
      continue;
    }
    seen[c.toLowerCase()] = true;
  }

  return Object.keys(seen).length;
}



