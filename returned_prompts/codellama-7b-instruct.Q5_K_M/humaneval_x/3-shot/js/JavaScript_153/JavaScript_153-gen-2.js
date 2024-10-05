  var strongest_extension = '';
  var strongest_strength = 0;

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
    if (strength >= strongest_strength) {
      strongest_strength = strength;
      strongest_extension = extension;
    }
  }
  return class_name + '.' + strongest_extension;
}



