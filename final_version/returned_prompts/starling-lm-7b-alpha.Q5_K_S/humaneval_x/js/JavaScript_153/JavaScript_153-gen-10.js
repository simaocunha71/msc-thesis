  let max = 0;
  let max_ext = "";
  for (const ext of extensions) {
    let strength = (ext.match(/[A-Z]/g) || []).length - (ext.match(/[a-z]/g) || []).length;
    if (strength > max) {
      max = strength;
      max_ext = ext;
    }
  }
  return class_name + "." + max_ext;
}



