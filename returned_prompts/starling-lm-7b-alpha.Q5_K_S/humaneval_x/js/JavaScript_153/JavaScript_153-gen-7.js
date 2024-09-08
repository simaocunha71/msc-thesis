  let strength = 0;
  let strongest_extension = null;
  for (const ext of extensions) {
    let ext_strength = (ext.match(/[A-Z]/g) || []).length - (ext.match(/[a-z]/g) || []).length;
    if (ext_strength >= strength) {
      strength = ext_strength;
      strongest_extension = ext;
    }
  }
  return class_name + '.' + strongest_extension;
}



