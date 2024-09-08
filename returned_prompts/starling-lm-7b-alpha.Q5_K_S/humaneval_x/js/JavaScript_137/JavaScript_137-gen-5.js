  if (typeof a === 'number' && typeof b === 'number') {
    return a > b ? a : b === a ? null : b;
  } else if (typeof a === 'string' && typeof b === 'string') {
    const reg = /^\d+(\.\d+)?$/;
    if (!reg.test(a) || !reg.test(b)) {
      return null;
    }
    const a_num = parseFloat(a);
    const b_num = parseFloat(b);
    return a_num > b_num ? a : b === a_num ? null : b;
  } else {
    return null;
  }
}



