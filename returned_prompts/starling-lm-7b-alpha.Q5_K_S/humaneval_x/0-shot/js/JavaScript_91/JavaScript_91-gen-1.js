    let counter = 0;
    let i = 0;
    while (i < S.length) {
      if (S[i] === 'I') {
        counter++;
        i += 2;
      } else {
        while (i < S.length && S[i] !== 'I') {
          i++;
        }
      }
    }
    return counter;
  };

  console.log(isBored("Hello world")); // 0
  console.log(isBored("The sky is blue. The sun is shining. I love this weather")); // 1
  console.log(isBored("I'm feeling great! I love programming.")); // 2
  console.log(isBored("I love programming.")); // 1
  console.log(isBored("I love programming.")); // 1
  console.log(isBored("I love programming. It's great.")); // 2
  console.log(isBored("It's great.")); // 0
  console.log(isBored("It's great. It's awesome.")); // 0
  console.log(isBored("It's great. It's awesome. I love this.")); // 1
  console.log(isBored("It's great. It's awesome. I love this.")); // 1
  console.log(isBored("It's great. It's awesome. I love this.")); // 1

































































































































































