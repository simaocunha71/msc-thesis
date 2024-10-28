  let count = 0;
  const vowels = "aeiou";
  for  (let i = 0; i < s.length; i++) {
    if  (vowels.includes(s[i].toLowerCase())) {
      count++;
    }
  }
  if  (s[s.length - 1] === "y") {
    count++;
  }
  return count;
}



