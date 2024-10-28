  if (arr.length == 0) return null;
  let sum = 0;
  let product_signs = 1;

  for (let i = 0; i < arr.length; i++) {
    let magnitude = Math.abs(arr[i]);
    sum += magnitude;
    if (arr[i] < 0) product_signs *= -1;
  }

  return sum * product_signs;
}

Please check my answers and give me feedback.
I would like to improve my programming skills.