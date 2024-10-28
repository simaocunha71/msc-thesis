  for (let i = 0; i < a.length; i++) {
    const pattern = a.slice(i);
    const pattern_rotations = [pattern, pattern.slice(1), pattern.slice(2), pattern.slice(3)];
    for (const pattern_rotation of pattern_rotations) {
      if (b.includes(pattern_rotation)) {
        return true;
      }
    }
  }
  return false;
}



