  if (txt.match(/\s/) != null) {
    return txt.split(/\s+/);
  } else if (txt.match(/,/) != null) {
    return txt.split(/,+/);
  } else {
    var sum = 0;
    for (var i = 0; i < txt.length; i++) {
      sum += (txt[i].charCodeAt(0) % 2 == 0) ? 0 : 1;
    }
    return sum;
  }
}



