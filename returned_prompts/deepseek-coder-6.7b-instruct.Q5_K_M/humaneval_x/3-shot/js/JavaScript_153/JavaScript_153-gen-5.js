  let maxStrength = -Infinity, strongestExtension = '';
  for (let ext of extensions) {
    let cap = (ext.match(/[A-Z]/g) || []).length;
    let sm = (ext.match(/[a-z]/g) || []).length;
    let strength = cap - sm;
    if (strength > maxStrength) {
      maxStrength = strength;
      strongestExtension = ext;
    }
  }
  return `${class_name}.${strongestExtension}`;
}



