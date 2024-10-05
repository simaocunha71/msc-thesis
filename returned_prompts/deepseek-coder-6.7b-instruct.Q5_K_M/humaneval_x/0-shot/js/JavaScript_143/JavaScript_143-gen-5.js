  // Initialize an empty string to store the result
  let result = '';

  // Split the sentence into an array of words
  const words = sentence.split(' ');

  // Function to check if a number is prime
  const isPrime = (num) => {
    if (num < 2) return false;
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if (num % i === 0) return false;
    return true;
  }

  // Iterate over the words
  for (let word of words) {
    // If the length of the word is prime, add it to the result
    if (isPrime(word.length)) result += word + ' ';
  }

  // Return the result string, removing the trailing space
  return result.trim();
}
```

## 3. 프로그래밍 문제 해설

- 주어진 문장을 단어로 나눈다.
- 단어의 길이가 소수인지 확인한다.
- 그렇다면 결과 문자열에 추가한다.
- 모든 단어를 확인한 후, 결과 문자열을 반환한다.

## 4. 시간 복잡도

- 문장의 길이를 n이라고 하면, 우리