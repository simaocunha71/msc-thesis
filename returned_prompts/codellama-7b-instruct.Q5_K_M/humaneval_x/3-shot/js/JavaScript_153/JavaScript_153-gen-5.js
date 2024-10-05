  var max_strength = 0;
  var strongest_extension = '';
  for (const ext of extensions) {
    var strength = 0;
    for (const c of ext) {
      if (c == c.toUpperCase()) {
        strength++;
      }
    }
    strength -= ext.length;
    if (strength > max_strength) {
      max_strength = strength;
      strongest_extension = ext;
    } else if (strength == max_strength) {
      if (extensions.indexOf(ext) < extensions.indexOf(strongest_extension)) {
        max_strength = strength;
        strongest_extension = ext;
      }
    }
  }
  return class_name + '.' + strongest_extension;
}



