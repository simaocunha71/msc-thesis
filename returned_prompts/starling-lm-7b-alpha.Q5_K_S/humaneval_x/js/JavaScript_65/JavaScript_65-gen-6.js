  const s = x.toString();
  let first = s[0];
  let last = s[s.length - 1];

  if (shift >= s.length) {
    return s.split('').reverse().join('');
  } else {
    return s.slice(shift)
            .concat(s.slice(0, shift))
            .join('');
  }
}



