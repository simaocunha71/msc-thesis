const strongestExtension = (class_name, extensions) => {
  let bestExtension = null;
  let bestStrength = -Infinity;
  for (let extension of extensions) {
    const extensionName = extension.toLowerCase();
    const strength = extensionName.replace(/[^a-z]/g, '').length - extensionName.replace(/[^A-Z]/g, '').length;
    if (strength > bestStrength) {
      bestStrength = strength;
      bestExtension = extension;
    }
  }
  return `${class_name}.${bestExtension}`;
}

