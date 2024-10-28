  let max_strength = -Infinity;
  let strongest_extension = '';

  for (const extension of extensions) {
    let cap = extension.split('').filter(c => c.toUpperCase() === c).length;
    let sm = extension.split('').filter(c => c.toLowerCase() === c).length;
    let strength = cap - sm;

    if (strength > max_strength) {
      max_strength = strength;
      strongest_extension = extension;
    }
  }

  return class_name + '.' + strongest_extension;
}