  let strongest_extension = extensions[0];
  let strongest_strength = 0;

  for (const extension of extensions) {
    let strength = extension.split('').reduce((acc, c) => {
      if (c >= 'A' && c <= 'Z') {
        return acc + 1;
      } else if (c >= 'a' && c <= 'z') {
        return acc - 1;
      }
      return acc;
    }, 0);
    if (strength > strongest_strength) {
      strongest_extension = extension;
      strongest_strength = strength;
    }
  }

  return `${class_name}.${strongest_extension}`;
}