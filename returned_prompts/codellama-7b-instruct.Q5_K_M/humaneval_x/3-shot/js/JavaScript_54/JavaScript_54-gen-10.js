  var c = new Set(s0);
  for (var i = 0; i < s1.length; i++) {
    if (!c.has(s1[i])) {
      return false;
    }
  }
  return true;
}



