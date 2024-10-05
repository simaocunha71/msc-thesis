  // 1.
  const hasCloseElements = (numbers, threshold) => {
    for (let i = 0; i < numbers.length; i++) {
      for (let j = 0; j < numbers.length; j++) {
        if (i !== j) {
          const distance = Math.abs(numbers[i] - numbers[j]);
          if (distance < threshold) {
            return true;
          }
        }
      }
    }
    return false;
  };

  // 2.
  const separateParenGroups = (parenString) => {
    const result = [];
    let currentString = [];
    let currentDepth = 0;

    for (const c of parenString.replace(/\s/g, '')) {
      if (c === '(') {
        currentDepth += 1;
        currentString.push(c);
      } else if (c === ')') {
        currentDepth -= 1;
        currentString.push(c);
        if (currentDepth === 0) {
          result.push(currentString.join(''));
          currentString = [];
        }
      }
    }

    return result;
  };

  // 3.
  const truncateNumber = (number) => {
    return number % 1;
  };

  // 4.
  const findClosestElements = (numbers) => {
    let minDiff, minPair;
    numbers.sort((a, b) => a - b);

    for (let i = 0; i