  var unique = '';
  for (const c of string) {
    if (unique.indexOf(c) == -1) {
      unique += c;
    }
  }

  return unique.length;
}



