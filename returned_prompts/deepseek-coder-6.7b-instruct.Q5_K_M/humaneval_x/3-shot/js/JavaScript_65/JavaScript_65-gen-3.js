  let digits = String(x).split('');
  if (shift >= digits.length) {
    return digits.reverse().join('');
  } else {
    let shifted = digits.splice(-shift);
    return [...shifted, ...digits].join('');
  }
}



