  return (x === n ** Math.floor(Math.log(x) / Math.log(n)));
  // Math.log(x) / Math.log(n) is a fraction that gives the integer power that x is a power of n
  // Math.floor(Math.log(x) / Math.log(n)) gives the integer power that x is a power of n
  // x === n ** Math.floor(Math.log(x) / Math.log(n)) checks if the number x is a simple power of n

  // Alternatively
  return (x === n ** Math.log(x) / Math.log(n));

  // Math.log(x) / Math.log(n) is a fraction that gives the integer power that x is a power of n
  // x === n ** Math.log(x) / Math.log(n) checks if the number x is a simple power of n

  // Alternatively
  return (x === n ** (Math.log(x) / Math.log(n)));

  // Math.log(x) / Math.log(n) is a fraction that gives the integer power that x is a power of n
  // x === n ** (Math.log(x) / Math.log(n)) checks if the number x is a simple power of n

  // Alternatively
  return (x === n ** (Math.log(x) / Math.LN10));

  // Math.LN10 is the natural logarithm of 10
  // Math.log(x) / Math.LN10 is a fraction that gives the integer power that x is a power of n
  // x === n ** (Math.log(x) / Math.LN10)) checks if the number x is a simple power of n

  // Alternatively
  return (x === n ** (Math.log10(x)));

  // Math.log10(x) is the integer power that x is a power of n
  // x === n ** (Math.log10(x)) checks if the number x is a simple power of n

  // Alternatively
  return (x === n ** (Math.log10(x) | 0));
