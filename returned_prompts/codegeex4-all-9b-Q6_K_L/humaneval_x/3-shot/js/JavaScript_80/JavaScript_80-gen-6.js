  for (let i = 0; i < s.length; i += 3) {
    if (s[i] == s[i + 1] || s[i] == s[i + 2] || s[i + 1] == s[i + 2]) {
      return false;
    }
  }
  return true;
}



