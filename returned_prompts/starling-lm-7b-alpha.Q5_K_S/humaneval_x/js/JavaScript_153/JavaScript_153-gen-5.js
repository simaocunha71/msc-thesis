  let class_name_length = class_name.length;

  let max_strength = -class_name_length;
  let strongest_extension = class_name;

  for (const extension of extensions) {
    let extension_name_length = extension.length;
    let up_case_count = 0;
    let low_case_count = 0;

    for (const c of extension) {
      if (c >= 'A' && c <= 'Z') {
        up_case_count += 1;
      } else if (c >= 'a' && c <= 'z') {
        low_case_count += 1;
      }
    }

    let strength = up_case_count - low_case_count;
    if (strength >= max_strength) {
      max_strength = strength;
      strongest_extension = extension;
    }
  }

  return `${class_name}.${strongest_extension}`;
}



