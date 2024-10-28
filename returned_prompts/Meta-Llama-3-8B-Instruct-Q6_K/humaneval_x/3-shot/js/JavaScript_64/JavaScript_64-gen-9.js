  let count = 0;
  for (let i = 0; i < s.length; i++) {
    switch (s[i].toLowerCase()) {
      case 'a':
      case 'e':
      case 'i':
      case 'o':
      case 'u':
      case 'y':
        if (i === s.length - 1) {
          count++;
          break;
        }
        if (s[i + 1].toLowerCase() !== 'y') {
          count++;
        }
    }
  }
  return count;
}