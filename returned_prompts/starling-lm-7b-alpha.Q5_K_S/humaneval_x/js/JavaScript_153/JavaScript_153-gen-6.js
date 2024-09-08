  const cap = (c) => {
    return c.toUpperCase() == c ? 1 : 0;
  };
  const sm = (c) => {
    return c.toLowerCase() == c ? 1 : 0;
  };
  const score = (c) => {
    return cap(c) - sm(c);
  };
  const max = (a, b) => {
    if (a > b) {
      return a;
    }
    return b;
  };

  let strength = {
    name: '',
    score: -1
  };

  for (const ext of extensions) {
    if (ext.length > strength.score) {
      strength = {
        name: ext,
        score: score(ext)
      };
    }
  }

  return class_name + '.' + strength.name;
};



