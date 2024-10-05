  var strongest = -Infinity;
  var strongest_index = -1;

  for (let i = 0; i < extensions.length; i++) {
    let extension = extensions[i];
    let cap = 0;
    let sm = 0;
    for (let c of extension) {
      if (c.toUpperCase() == c) {
        cap++;
      } else if (c.toLowerCase() == c) {
        sm++;
      }
    }
    let strength = cap - sm;
    if (strength > strongest) {
      strongest = strength;
      strongest_index = i;
    } else if (strength == strongest && extensions[strongest_index].localeCompare(extension) > 0) {
      strongest_index = i;
    }
  }
  return class_name + '.' + extensions[strongest_index];
}



