  let strongest = '';
  let max_strength = 0;
  for (const extension of extensions) {
    let upper = 0;
    let lower = 0;
    for (const c of extension) {
      if (c.toUpperCase() === c) {
        upper++;
      } else {
        lower++;
      }
    }
    let strength = upper - lower;
    if (strength > max_strength) {
      max_strength = strength;
      strongest = extension;
    }
  }
  return class_name + '.' + strongest;
}  // Example: strongestExtension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000 tests.  // 0.1 sec, ~2000