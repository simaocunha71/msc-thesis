  const odd_length_words = lst.filter(word => word.length % 2 !== 0);
  lst = lst.filter(word => word.length % 2 === 0);
  lst.sort((a, b) => a.length - b.length || a.localeCompare(b));
  return lst.concat(odd_length_words);
}



