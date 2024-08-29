  let strongest_extension = '';
  let strongest_strength = 0;
  for (const extension of extensions) {
    let strength = (extension.match(/[A-Z]/g) || []).length - (extension.match(/[a-z]/g) || []).length;
    if (strength > strongest_strength || (strength == strongest_strength && extension < strongest_extension)) {
      strongest_strength = strength;
      strongest_extension = extension;
    }
  }
  return class_name + '.' + strongest_extension;
}



