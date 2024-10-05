  return sentence.split(' ').filter((word) => {
    return word.length % 2 == 1;
  }).join(' ');
}



