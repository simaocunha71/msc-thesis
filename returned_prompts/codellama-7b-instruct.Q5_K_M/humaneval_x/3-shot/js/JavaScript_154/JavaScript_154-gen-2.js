  var a_rotated = a.split('').reverse().join('');

  if (a.includes(b) || a_rotated.includes(b)) {
    return true;
  }

  return false;
}



