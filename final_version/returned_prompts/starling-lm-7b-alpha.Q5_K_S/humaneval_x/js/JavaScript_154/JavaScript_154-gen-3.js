  let b_rotations = [];
  for (let i = 0; i < b.length; i++) {
    b_rotations.push(b.slice(i) + b.slice(0, i));
  }
  for (let i = 0; i < b_rotations.length; i++) {
    if (a.indexOf(b_rotations[i]) > -1) {
      return true;
    }
  }
  return false;
}



