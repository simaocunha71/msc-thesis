  if (typeof a == typeof b) {
    if (a == b) {
      return null;
    } else if (a > b) {
      return a;
    } else {
      return b;
    }
  } else {
    let a_number = Number(a);
    let b_number = Number(b);
    if (Number.isNaN(a_number) || Number.isNaN(b_number)) {
      return null;
    } else if (a_number > b_number) {
      return a_number;
    } else {
      return b_number;
    }
  }
}