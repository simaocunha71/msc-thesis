  let strongest = [0, ''];
  for (let ext of extensions) {
    let cap = Array.from(ext).filter(x => x === x.toUpperCase()).length;
    let sm = Array.from(ext).filter(x => x === x.toLowerCase()).length;
    let strength = cap - sm;
    if (strength > strongest[0]) {
      strongest = [strength, ext];
    }
  }
  return `${class_name}.${strongest[1]}`;
}



