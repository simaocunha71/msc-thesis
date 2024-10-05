  let max_word = null;
  let max_count = 0;

  for  (let word of words)  {
    let unique_chars = new Set(word.split(''));
    let count = unique_chars.size;

    if  (count > max_count)  {
      max_count = count;
      max_word = word;
    } 
    else if  (count == max_count)  {
      max_word = max_word < word ? max_word : word;
    }
  }

  return max_word;
}



