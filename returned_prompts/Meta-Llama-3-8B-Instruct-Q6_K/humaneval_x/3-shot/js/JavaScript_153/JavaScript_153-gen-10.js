  let strongest = { name: extensions[0], strength: 0 };
  for (let i = 0; i < extensions.length; i++) {
    let extension = extensions[i];
    let cap = extension.match(/[A-Z]/g).length;
    let sm = extension.match(/[a-z]/g).length;
    let strength = cap - sm;
    if (strength > strongest.strength) {
      strongest = { name: extension, strength: strength };
    }
  }
  return class_name + '.' + strongest.name;
}