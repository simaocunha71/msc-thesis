  let result = 0;
  let remCount = [0, 0, 0];

  for (let i = 1; i <= n; i++) {
    let val = Math.floor(i * i - i + 1) % 3;
    remCount[val]++;
  }

  result += Math.floor(remCount[0] * (remCount[0] - 1) * (remCount[0] - 2) / 6);
  result += Math.floor(remCount[1] * (remCount[1] - 1) * (remCount[1] - 2) / 6);
  result += remCount[2] * remCount[1] * remCount[0];
  result += Math.floor(remCount[2] * (remCount[2] - 1) * (remCount[2] - 2) / 6);

  return result;
}



