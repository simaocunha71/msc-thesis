function uniqueTokens(str1, str2) {
  var tokens1 = str1.split(" ");
  var tokens2 = str2.split(" ");
  var unique = "";
  for (var i = 0; i < tokens1.length; i++) {
    var token1 = tokens1[i];
    var found = false;
    for (var j = 0; j < tokens2.length; j++) {
      if (tokens2[j] == token1) {
        found = true;
        break;
      }
    }
    if (!found) {
      unique += token1 + " ";
    }
  }
  return unique;
}

