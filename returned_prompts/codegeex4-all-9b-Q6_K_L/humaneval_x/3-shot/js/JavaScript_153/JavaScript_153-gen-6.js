  let max = -2;
  let max_index = -1;

  for (let i = 0; i < extensions.length; i++) {
    let strength = 0;
    for (let j = 0; j < extensions[i].length; j++) {
      if (extensions[i][j] == extensions[i][j].toUpperCase()) {
        strength += 1;
      } else {
        strength -= 1;
      }
    }

    if (strength > max) {
      max = strength;
      max_index = i;
    }
  }

  return `${class_name}.${extensions[max_index]}`;
}