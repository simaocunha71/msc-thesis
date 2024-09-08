  let b_rotations = Array.from(b).map(el => b.slice(b.indexOf(el) + 1) + el);
  return b_rotations.some(el => a.indexOf(el) > -1);
}



