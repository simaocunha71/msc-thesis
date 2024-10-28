  strings.sort((a, b) => {
    let a_count = 0;
    let b_count = 0;
    for (let i = 0; i < a.length; i++) {
      if (a[i] == 'a') {
        a_count += 1;
      }
    }
    for (let i = 0; i < b.length; i++) {
      if (b[i] == 'a') {
        b_count += 1;
      }
    }
    if (a_count != b_count) {
      return b_count - a_count;
    } else {
      return a.localeCompare(b);
    }
  });
  return strings;
}