  let num = parseFloat(value);
  return num >= 0 ? Math.ceil(num) : Math.floor(num);
} // Math.ceil rounds up and Math.floor rounds down, so this function will always round away from zero.