  let max_strength = -Infinity;
  let strongest_extension = null;

  for (const extension of extensions) {
    let cap = 0;
    let sm = 0;
    for (const c of extension) {
      if (c.toUpperCase() == c) {
        cap += 1;
      } else {
        sm += 1;
      }
    }
    let strength = cap - sm;
    if (strength > max_strength) {
      max_strength = strength;
      strongest_extension = extension;
    }
  }
  return class_name + '.' + strongest_extension;
}