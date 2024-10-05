  if (strings.length == 0) {
    return null;
  }

  var longest_string = strings[0];
  for (let i = 1; i < strings.length; i++) {
    if (strings[i].length > longest_string.length) {
      longest_string = strings[i];
    }
  }

  return longest_string;
}



