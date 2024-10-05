    const maxUnique = (str) => {
      let count = 0;
      let unique = {};
      for(let i = 0; i < str.length; i++) {
        if(!unique[str[i]]) {
          unique[str[i]] = true;
          count++;
        }
      }
      return count;
    };

    let max = 0;
    let maxString = "";

    for(let i = 0; i < words.length; i++) {
      if(maxUnique(words[i]) > max) {
        max = maxUnique(words[i]);
        maxString = words[i];
      }
    }

    return maxString;
  };

  // Change code above this line

  console.log(findMax(["name", "of", "string"])); // "string"
  console.log(findMax(["name", "enam", "game"])); // "enam"
  console.log(findMax(["aaaaaaa", "bb", "cc"])); // "aaaaaaa"
  console.log(findMax(["hello", "world", "foo"])); // "hello"
  console.log(findMax(["apple", "banana", "pear"])); // "banana"















































































































































































































