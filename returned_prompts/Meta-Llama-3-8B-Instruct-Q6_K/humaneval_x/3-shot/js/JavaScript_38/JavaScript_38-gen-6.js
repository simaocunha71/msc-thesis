  let decoded = '';
  let groups = s.split('');
  for (let i = 0; i < groups.length; i++) {
    if (i % 3 == 0) {
      decoded += groups[i];
    } else {
      decoded = groups[i - 1] + decoded;
    }
  }
  return decoded;
}