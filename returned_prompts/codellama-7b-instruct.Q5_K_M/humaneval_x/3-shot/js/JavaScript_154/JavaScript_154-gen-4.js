  var result = false;
  for (let i = 0; i < a.length; i++) {
    var rotations = a.slice(i);
    rotations += a.slice(0, i);
    if (rotations.includes(b)) {
      result = true;
      break;
    }
  }
  return result;
}



