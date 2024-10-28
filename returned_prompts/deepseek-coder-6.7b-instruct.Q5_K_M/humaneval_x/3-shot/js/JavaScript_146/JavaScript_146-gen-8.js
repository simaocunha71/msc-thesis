  return nums.filter(n => n > 10 && `${Math.abs(n)}`[0] % 2 === 1 && `${Math.abs(n)}`.slice(-1) % 2 === 1).length;
}



