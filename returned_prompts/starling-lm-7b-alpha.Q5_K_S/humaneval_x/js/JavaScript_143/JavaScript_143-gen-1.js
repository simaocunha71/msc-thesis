  let words = sentence.split(" ");
  let result = "";

  for (const word of words) {
    if (isPrime(word.length)) {
      result += word + " ";
    }
  }

  return result.substring(0, result.length - 1);
}



