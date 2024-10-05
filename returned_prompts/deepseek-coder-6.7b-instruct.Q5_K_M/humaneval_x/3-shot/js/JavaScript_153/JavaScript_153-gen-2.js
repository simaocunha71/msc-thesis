  let strongest = [null, -Infinity];
  for (let ext of extensions) {
    let cap = [...ext].filter(x => x === x.toUpperCase()).length;
    let sm = [...ext].filter(x => x === x.toLowerCase()).length;
    let diff = cap - sm;
    if (diff > strongest[1]) {
      strongest = [ext, diff];
    }
  }
  return `${class_name}.${strongest[0]}`;
}



