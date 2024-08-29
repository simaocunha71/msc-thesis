  let result = false;

  for (let i = 0; i < string.length; i++) {
    if (string[i] == '[') {
      let left = 0;
      let right = 0;
      for (let j = i + 1; j < string.length; j++) {
        if (string[j] == '[') {
          left++;
        } else {
          right++;
        }
        if (left > right) {
          result = true;
          break;
        }
      }
    }
  }

  return result;
}



