  if (s.length < 3) return false;
  var list = [];
  for (var i = 0; i < 3; i++) {
    if (!list.includes(s[i])) {
      list.push(s[i]);
    } else {
      return false;
    }
  }
  for (var i = 3; i < s.length; i++) {
    list.shift();
    if (!list.includes(s[i])) {
      list.push(s[i]);
    } else {
      return false;
    }
  }
  return true;
}



