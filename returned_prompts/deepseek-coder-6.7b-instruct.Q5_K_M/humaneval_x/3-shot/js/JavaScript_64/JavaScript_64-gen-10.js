  let count = 0;
  let vowels =  ['a', 'e', 'i', 'o', 'u'];

  for  (let char of s.toLowerCase())  {
    if  (vowels.includes(char))  {
      count++;
     }
   }

  if  (s[s.length - 1]  ===  'y')  {
    count++;
  }

  return count;
}



