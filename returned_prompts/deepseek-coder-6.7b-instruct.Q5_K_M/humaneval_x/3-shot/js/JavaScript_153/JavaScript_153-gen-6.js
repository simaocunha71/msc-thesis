  let maxStrength = -Infinity, strongestExt = '';
  for (let ext of extensions) {
    let cap = Array.from(ext).filter(letter => letter === letter.toUpperCase()).length;
    let sm = Array.from(ext).filter(letter => letter === letter.toLowerCase()).length;
    let strength = cap - sm;
    if (strength > maxStrength) {
      maxStrength = strength;
      strongestExt = ext;
    }
  }
  return `${class_name}.${strongestExt}`;
}



