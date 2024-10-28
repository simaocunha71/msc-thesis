  let vowels  ["a","e","i","o","u"];
  let count =  0;
  let last_character  s[s.length  - 1];
  for  (let  i  in s)  {
    if  (vowels.includes(s[i]))  count++;
  }
  if  (last_character  in "yY")  count++;
  return count;
}



