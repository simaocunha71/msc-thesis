  let max_strength = -Infinity;
  let strongest_extension = "";
  for (let extension of extensions) {
    let strength = extension.split('').reduce((acc, char) => {
      return char === char.toUpperCase() ? acc + 1 : acc - 1;
    }, 0);
    if (strength > max_strength) {
      max_strength = strength;
      strongest_extension = extension;
    }
  }
  return `${class_name}.${strongest_extension}`;
}



