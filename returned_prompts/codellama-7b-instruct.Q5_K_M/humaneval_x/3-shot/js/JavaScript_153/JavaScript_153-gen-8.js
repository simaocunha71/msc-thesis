  var strengths = [];
  var extension_names = [];
  var strongest_extension = '';

  for (const extension of extensions) {
    var cap_count = 0;
    var sm_count = 0;

    for (const c of extension) {
      if (c.toUpperCase() == c) cap_count += 1;
      if (c.toLowerCase() == c) sm_count += 1;
    }

    strengths.push(cap_count - sm_count);
    extension_names.push(extension);
  }

  var index_of_max = strengths.indexOf(Math.max(...strengths));
  return `${class_name}.${extension_names[index_of_max]}`;
}



