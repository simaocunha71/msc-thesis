  let count = 0;

  for (let i = 0; i < num.length; i++) {
    let n = num[i];
    switch (n) {
      case 'A':
      case 'B':
      case 'D':
        count++;
        break;
      case 'E':
        if (num[i + 1] === 'D') {
          count++;
        }
        break;
      case 'F':
        if (num[i + 1] === 'D') {
          count++;
        }
        break;
    }
  }

  return count;
}



