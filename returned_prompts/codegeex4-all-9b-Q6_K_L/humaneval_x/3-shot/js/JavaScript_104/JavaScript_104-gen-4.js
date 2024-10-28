  return x.filter(num => {
    const digits = num.toString().split('');
    return !digits.some(digit => digit % 2 === 0);
  }).sort((a, b) => a - b);
}



