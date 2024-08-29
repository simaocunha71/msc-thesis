  const keys = Object.keys(dict);
  const values = Object.values(dict);
  return keys.every((key) => {
    return typeof key === 'string' && key.toLowerCase() === key.toUpperCase();
  }) || values.every((value) => {
    return typeof value === 'string' && value.toLowerCase() === value.toUpperCase();
  });
}



