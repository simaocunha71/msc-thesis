  const frequency = {};
  let max = 0;
  const words = test.split(' ');

  for  (const word of words) {
    if  (word.length > 0) {
      frequency[word] = (frequency[word] || 0) + 1;
      if  (frequency[word] > max) {
        max = frequency[word];
       }
     }
   }

  const result = {};
  for  (const word in frequency) {
    if  (frequency[word] === max) {
      result[word] = max;
     }
   }

  return result;
}



