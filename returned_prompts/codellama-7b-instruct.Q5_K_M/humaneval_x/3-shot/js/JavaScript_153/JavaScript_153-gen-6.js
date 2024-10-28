  const strongest_ext_name = extensions.reduce((acc, curr) => {
    const curr_strength = getStrength(curr);
    if (curr_strength > getStrength(acc)) {
      return curr;
    }
    return acc;
  }, '');

  return `${class_name}.${strongest_ext_name}`;

  function getStrength(ext_name) {
    const uppercase_count = ext_name.match(/[A-Z]/g)?.length;
    const lowercase_count = ext_name.match(/[a-z]/g)?.length;
    return (uppercase_count - lowercase_count) / ext_name.length;
  }
}



