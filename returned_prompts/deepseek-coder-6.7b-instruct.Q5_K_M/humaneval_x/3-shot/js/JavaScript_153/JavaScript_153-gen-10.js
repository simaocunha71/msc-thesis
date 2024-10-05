  let strongest_extension = extensions[0];
  let max_strength = getStrength(extensions[0], class_name);

  for (let i = 1; i < extensions.length; i++) {
    let strength = getStrength(extensions[i], class_name);
    if (strength > max_strength) {
      max_strength = strength;
      strongest_extension = extensions[i];
    }
  }

  return `${class_name}.${strongest_extension}`;
}

const getStrength = (extension, class_name) => {
  let cap = countUpperCase(extension, class_name);
  let sm = countLowerCase(extension, class_name);
  return cap - sm;
}

const countUpperCase = (extension, class_name) => {
  return (extension.split(class_name).join('') + extension).split('').reduce((acc, char) => {
    return acc + (char === char.toUpperCase() ? 1 : 0);
  }, 0);
}

const countLowerCase = (extension, class_name) => {
  return (extension.split(class_name).join('') + extension).split('').reduce((acc, char) => {
    return acc + (char === char.toLowerCase() ? 1 : 0);
  }, 0);
}



