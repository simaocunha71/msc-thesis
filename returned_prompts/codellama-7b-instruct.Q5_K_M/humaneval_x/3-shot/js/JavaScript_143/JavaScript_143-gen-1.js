  const words = sentence.split(' ');
  const prime_words = words.filter((word) => {
    let isPrime = true;
    for (let i = 2; i < Math.sqrt(word.length); i++) {
      if (word.length % i === 0) {
        isPrime = false;
        break;
      }
    }
    return isPrime;
  });
  return prime_words.join(' ');
}



