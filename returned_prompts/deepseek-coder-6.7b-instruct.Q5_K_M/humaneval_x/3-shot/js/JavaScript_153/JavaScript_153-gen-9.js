  let strongest = [0, ""];
  for (let ext of extensions) {
    let strength = ext.split('').reduce((acc, char) => {
      return char < 'a' ? acc + 1 : acc - 1;
    }, 0);
    if (strength > strongest[0]) {
      strongest = [strength, ext];
    }
  }
  return `${class_name}.${strongest[1]}`;
}



