  var max_extension = '';
  var max_strength = -1;

  for (let extension of extensions) {
    var strength = 0;
    for (let i = 0; i < extension.length; i++) {
      if (extension[i].match(/[A-Z]/)) {
        strength++;
      }
    }

    strength = strength - extension.length + extension.match(/[a-z]/g).length;

    if (strength > max_strength) {
      max_extension = extension;
      max_strength = strength;
    }
  }

  return class_name + '.' + max_extension;
}



