  const class_length = class_name.length;
  let max_strength = -class_length;
  let strongest_ext = "";

  for (const ext of extensions) {
    const ext_len = ext.length;
    const cap = ext.match(/[A-Z]/g) || [];
    const sm = ext.match(/[a-z]/g) || [];
    const strength = (cap.length - sm.length) / ext_len;

    if (strength >= max_strength) {
      max_strength = strength;
      strongest_ext = ext;
    }
  }

  return `${class_name}.${strongest_ext}`;
}



