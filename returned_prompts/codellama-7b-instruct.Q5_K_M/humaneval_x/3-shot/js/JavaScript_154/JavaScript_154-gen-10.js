  var rot = 1;
  var isrot = false;
  var i = 0;

  while (i < a.length) {
    var rotated = rotate(a, rot);
    if (rotated.includes(b)) {
      return true;
    }
    rot++;
    i++;
  }
  return false;
}



