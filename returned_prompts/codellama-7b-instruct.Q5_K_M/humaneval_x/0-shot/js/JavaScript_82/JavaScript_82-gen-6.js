
  function primeLength(str) {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
      if (str[i] === " ") {
        count++;
      }
    }
    if (str.length % count === 0) {
      return true;
    } else {
      return false;
    }
  }

  primeLength("Hello");
  primeLength("abcdcba");
  primeLength("kittens");
  primeLength("orange");

Answer: 

  const primeLength = (string) => {
    let count = 0;
    for (let i = 0; i < string.length; i++) {
      if (string[i] === " ") {
        count++;
      }
    }
    if (string.length % count === 0) {
      return true;
    } else {
      return false;
    }
  }

  primeLength("Hello");
  primeLength("abcdcba");
  primeLength("kittens");
  primeLength("orange");

