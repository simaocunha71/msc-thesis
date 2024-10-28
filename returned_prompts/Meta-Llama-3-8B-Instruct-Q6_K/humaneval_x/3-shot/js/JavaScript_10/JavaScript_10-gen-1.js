  var reversed = string.split('').reverse().join('');
  for (var i = 0; i < string.length; i++) {
    if (string.substring(i) + reversed.substring(i) === reversed) {
      return string + reversed.substring(i);
    }
  }
  return string + reversed;
}