  var strongest_extension = extensions[0];
  var strongest_strength = classStrength(extensions[0]);

  for (var i = 1; i < extensions.length; i++) {
    var strength = classStrength(extensions[i]);
    if (strength > strongest_strength) {
      strongest_extension = extensions[i];
      strongest_strength = strength;
    }
  }

  return class_name + '.' + strongest_extension;
}

const classStrength = (extension) => {
  var strength = 0;
  for (const c of extension) {
    if (c == c.toLowerCase()) {
      strength -= 1;
    } else {
      strength += 1;
    }
  }
  return strength;
}