  if (l.length < 2) return true;

  var diff = l[1] - l[0];
  for (var i = 1; i < l.length; i++) {
    if (diff * (l[i] - l[i - 1]) < 0) return false;
  }

  return true;
}



