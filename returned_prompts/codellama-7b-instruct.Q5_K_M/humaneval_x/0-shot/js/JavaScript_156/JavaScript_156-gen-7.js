/*
  Roman numerals use the following mapping:
    [1000] -> 'M'
    [900] -> 'CM'
    [500] -> 'D'
    [400] -> 'CD'
    [100] -> 'C'
    [90] -> 'XC'
    [50] -> 'L'
    [40] -> 'XL'
    [10] -> 'X'
    [9] -> 'IX'
    [5] -> 'V'
    [4] -> 'IV'
    [1] -> 'I'

  We can use the following rules:
    - The number is a power of 5:
      - If the number is a power of 5, we can represent it as a string of 'V's.
    - The number is a power of 10:
      - If the number is a power of 10, we can represent it as a string of 'X's.
    - The number is a power of 50:
      - If the number is a power of 50, we can represent it as a string of 'L's.
    - The number is a power of 100:
      - If the number is a power of 100, we can represent it as a string of 'C's.
    - The number is a power of 500:
      - If the number is a power of 500, we can represent it as a string of 'D's.
    - The number is a power of 1000:
      - If the number is a power of 1000, we can represent it as a string of 'M's.
    - The number is a sum of powers of 5, 10, 50, 100, and 1000:
      - If the number is a sum of powers of 5, 10, 50, 100, and 1000, we can represent it as a string of 'V's, 'X's, 'L's, 'C's, and 'M's.

  We can use the following