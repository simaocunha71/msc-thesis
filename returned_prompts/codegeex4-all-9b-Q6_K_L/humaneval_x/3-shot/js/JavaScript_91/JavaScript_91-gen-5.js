  var count = 0;
  var words = S.split(/[.?!]/);
  for (var i = 0; i < words.length; i++) {
    if (words[i].trim().startsWith('I')) {
      count += 1;
    }
  }
  return count;
}



