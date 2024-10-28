  const len_a = a.length;
  const len_b = b.length;
  for (let i = 0; i < len_b; i++) {
    const b_rot = b.slice(i) + b.slice(0, i);
    if (a.includes(b_rot)) {
      return true;
    }
  }
  return false;
}



