  var a_rotations = [];
  var b_rotations = [];

  for (var i = 0; i < a.length; i++) {
    a_rotations.push(a.slice(i) + a.slice(0, i));
  }

  for (var j = 0; j < b.length; j++) {
    b_rotations.push(b.slice(j) + b.slice(0, j));
  }

  for (var k = 0; k < a_rotations.length; k++) {
    for (var l = 0; l < b_rotations.length; l++) {
      if (a_rotations[k].includes(b_rotations[l])) {
        return true;
      }
    }
  }
  return false;
}



