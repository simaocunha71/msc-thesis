  var prefixes = [];
  for  (var i = 0; i < string.length; i++) {
    prefixes.push(string.slice(0, i+1));
  }
  return prefixes;
}



