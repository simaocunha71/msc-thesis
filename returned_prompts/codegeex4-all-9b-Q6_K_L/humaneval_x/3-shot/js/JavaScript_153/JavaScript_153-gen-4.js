  var max_strength = 0;
  var max_index = 0;

  for (let i = 0; i < extensions.length; i++) {
    let extension = extensions[i];
    let cap = 0;
    let sm = 0;

    for (const c of extension) {
      if (c == c.toUpperCase()) {
        cap += 1;
      } else {
        sm += 1;
      }
    }

    let strength = cap - sm;
    if (strength > max_strength) {
      max_strength = strength;
      max_index = i;
    }
  }

  return `${class_name}.${extensions[max_index]}`;
}



