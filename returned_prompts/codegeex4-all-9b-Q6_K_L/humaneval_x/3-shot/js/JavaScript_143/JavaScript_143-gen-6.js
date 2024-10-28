  let result = "";
  let words = sentence.split(' ');

  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    let isPrime = true;

    if (word.length < 2) {
      continue;
    }

    for (let j = 2; j < word.length; j++) {
      if (word.length % j == 0) {
        isPrime = false;
        break;
      }
    }

    if (isPrime) {
      result += word;
      if (i != words.length - 1) {
        result += ' ';
      }
    }
  }

  return result;
}