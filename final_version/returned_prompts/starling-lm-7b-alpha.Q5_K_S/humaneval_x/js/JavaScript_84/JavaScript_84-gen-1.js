  let sum = 0;
  let binary = '';
  while (N > 0) {
    sum += (N % 2);
    binary += (N % 2);
    N = Math.floor(N / 2);
  }
  return String(sum).padStart(binary.length, '0') + binary.split('').reverse().join('');
}



