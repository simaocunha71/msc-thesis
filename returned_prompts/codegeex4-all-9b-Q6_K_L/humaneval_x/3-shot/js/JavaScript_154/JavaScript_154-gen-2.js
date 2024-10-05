  let rotations = [];
  for (let i = 0; i < b.length; i++) {
    let rotation = b.slice(i) + b.slice(0, i);
    rotations.push(rotation);
  }

  for (const rotation of rotations) {
    if (a.includes(rotation)) {
      return true;
    }
  }

  return false;
}

