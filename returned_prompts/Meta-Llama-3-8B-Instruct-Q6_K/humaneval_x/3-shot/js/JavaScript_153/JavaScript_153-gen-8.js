  let strongest = null;
  let max_strength = -Infinity;

  for (const extension of extensions) {
    let cap = 0;
    let sm = 0;
    for (const c of extension) {
      if (c.toUpperCase() == c) {
        cap++;
      } else {
        sm++;
      }
    }
    let strength = cap - sm;
    if (strength > max_strength) {
      max_strength = strength;
      strongest = extension;
    }
  }
  return class_name + '.' + strongest;
}