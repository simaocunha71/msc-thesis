  let maxCount = 0;
  let maxWord;

  for  (const word of words)  {
    const uniqueCounts = new Set(word).size;
    if  (uniqueCounts > maxCount)  {
      maxCount = uniqueCounts;
      maxWord = word;
     } else if  (uniqueCounts === maxCount)  {
      maxWord = maxWord < word ? maxWord : word;
     }
   }

  return maxWord;
}



