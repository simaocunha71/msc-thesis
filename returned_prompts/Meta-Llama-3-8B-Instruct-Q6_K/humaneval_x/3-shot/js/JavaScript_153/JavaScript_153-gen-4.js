  let strongest = null;
  let strongest_strength = -Infinity;

  for (const extension of extensions) {
    let upper = 0;
    let lower = 0;
    for (const c of extension) {
      if (c.toUpperCase() === c) {
        upper++;
      } else {
        lower++;
      }
    }
    let strength = upper - lower;
    if (strength > strongest_strength) {
      strongest_strength = strength;
      strongest = extension;
    }
  }

  return class_name + '.' + strongest;
}