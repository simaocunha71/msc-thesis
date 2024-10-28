  var strongest_extension = extensions[0];
  for (var i = 1; i < extensions.length; i++) {
    var current_extension = extensions[i];
    if (strength(current_extension) > strength(strongest_extension)) {
      strongest_extension = current_extension;
    }
  }
  return class_name + '.' + strongest_extension;
}

const strength = (extension) => {
  var cap = 0;
  var sm = 0;
  for (const c of extension) {
    if (c == c.toUpperCase()) {
      cap += 1;
    } else if (c == c.toLowerCase()) {
      sm += 1;
    }
  }
  return cap - sm;
}