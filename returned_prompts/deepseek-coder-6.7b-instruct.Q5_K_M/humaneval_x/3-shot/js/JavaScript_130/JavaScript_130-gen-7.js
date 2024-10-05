  let sequence = [0, 3, 2];
  for(let i = 3; i <= n; i++){
    sequence[i] = (i % 2 === 0) ? 1 + i / 2 : sequence[i - 1] + sequence[i - 2] + sequence[i + 1];
  }
  return sequence;
}



