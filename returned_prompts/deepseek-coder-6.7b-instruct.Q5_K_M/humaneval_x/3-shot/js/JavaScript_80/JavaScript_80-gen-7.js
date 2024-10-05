  for  (let i = 2; i < s.length; i++) {
    if  (s[i] == s[i - 1] || s[i] == s[i - 2] || s[i - 1] == s[i - 2])  {
      return false;
    }
  }
  return s.length >= 3;
}



