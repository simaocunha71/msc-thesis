  let rotations = [];
  for (let i = 1; i < b.length; i++) {
    rotations.push(b.slice(i) + b.slice(0, i));
  }
  for (let i = 0; i < rotations.length; i++) {
    if (a.includes(rotations[i])) {
      return true;
    }
  }
  return false;
}



