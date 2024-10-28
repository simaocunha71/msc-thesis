  l.sort();
  var i = Math.floor(l.length / 2);
  if (l.length % 2 == 0) {
    return (l[i] + l[i - 1]) / 2.0;
  } else {
    return l[i];
  }
}



