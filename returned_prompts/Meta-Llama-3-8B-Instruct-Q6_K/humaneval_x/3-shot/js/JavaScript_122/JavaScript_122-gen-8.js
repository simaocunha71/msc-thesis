  let sum = 0;
  for (let i = 0; i < k; i++) {
    if (String(arr[i]).length <= 2) {
      sum += arr[i];
    } else {
      break;
    }
  }
  return sum;
}  // or return arr.slice(0, k).filter(x => String(x).length <= 2).reduce((a, b) => a + b, 0);  // this will work too
}  // the second approach is more elegant, but the first approach is more readable and understandable for beginners  // I would recommend the first approach for a beginner.