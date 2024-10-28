  let strongest_extension = '';
  let strongest_strength = -1;
  let strength_sum = 0;

  for (const extension of extensions) {
    let lowercase_count = 0;
    for (const c of extension) {
      if (c.toUpperCase() == c) {
        strength_sum += 1;
      } else {
        lowercase_count += 1;
      }
    }
    let strength = strength_sum - lowercase_count;
    if (strength > strongest_strength) {
      strongest_strength = strength;
      strongest_extension = extension;
    }
    strength_sum = 0;
  }

  return class_name + '.' + strongest_extension;
}



