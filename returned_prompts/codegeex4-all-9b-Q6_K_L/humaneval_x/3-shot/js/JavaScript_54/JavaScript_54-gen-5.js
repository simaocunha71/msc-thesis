  if (s0.length != s1.length) {
    return false;
  }

  const chars0 = s0.split('');
  const chars1 = s1.split('');

  for (let i = 0; i < chars0.length; i++) {
    const index = chars1.indexOf(chars0[i]);
    if (index == -1) {
      return false;
    }
    chars1.splice(index, 1);
  }

  return true;
}

