  var words = sentence.split(' ');

  for (var i = 0; i < words.length; i++) {
    if (isPrime(words[i].length)) {
      result += words[i] + ' ';
    }
  }

  return result.trim();
}



