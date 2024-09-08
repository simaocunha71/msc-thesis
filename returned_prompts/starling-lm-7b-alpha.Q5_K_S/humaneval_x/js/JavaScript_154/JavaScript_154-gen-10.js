  let bb = b.split("");
  for (let i = 0; i < bb.length; i++) {
    if (a.includes(bb[i])) {
      return true;
    }
    bb.push(bb.shift());
  }
  return false;
}



