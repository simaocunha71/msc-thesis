  let strongest = [null, -Infinity];
  for (let ext of extensions) {
    let diff = ext.match(/[A-Z]/g)?.length || 0
               - (ext.match(/[a-z]/g)?.length || 0);
    if (diff > strongest[1]) {
      strongest = [ext, diff];
    }
  }
  return `${class_name}.${strongest[0]}`;
}



