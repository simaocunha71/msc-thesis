  /*
    Write a function called isPrime that takes one parameter: a number.
    It should return true if the number is prime, false if it is not.
    The function should use no loops.
    The function should use no if statements.
    The function should use no ternary operators.
    The function should use no arrays.
    The function should use no object keys or methods.
    The function should use no regular expressions.
    The function should use no built in javascript methods.

    Examples:
    >>> isPrime(1)
    false
    >>> isPrime(2)
    true
    >>> isPrime(3)
    true
    >>> isPrime(4)
    false
    >>> isPrime(5)
    true
    */
  
  const isPrime = (num) => {
    return num > 1 && num % 2 && num % 3 && num % 5;
  }

