  let strongest = '';
  let max_strength = -Infinity;

  for (let extension of extensions) {
    let cap = 0;
    let sm = 0;
    for (let c of extension) {
      if (c.toUpperCase() === c) {
        cap++;
      } else {
        sm++;
      }
    }
    let strength = cap - sm;
    if (strength > max_strength) {
      strongest = extension;
      max_strength = strength;
    }
  }

  return class_name + '.' + strongest;
}  // Do not change the code above this line. Write your solution below this line.