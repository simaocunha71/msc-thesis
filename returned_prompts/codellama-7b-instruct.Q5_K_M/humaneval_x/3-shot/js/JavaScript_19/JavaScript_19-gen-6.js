  const sorted = numbers.split(' ').sort((a, b) => {
    if (a == 'zero' || b == 'zero') {
      return 0;
    }
    if (a == 'one' || b == 'one') {
      return 1;
    }
    if (a == 'two' || b == 'two') {
      return 2;
    }
    if (a == 'three' || b == 'three') {
      return 3;
    }
    if (a == 'four' || b == 'four') {
      return 4;
    }
    if (a == 'five' || b == 'five') {
      return 5;
    }
    if (a == 'six' || b == 'six') {
      return 6;
    }
    if (a == 'seven' || b == 'seven') {
      return 7;
    }
    if (a == 'eight' || b == 'eight') {
      return 8;
    }
    if (a == 'nine' || b == 'nine') {
      return 9;
    }
  });

  return sorted.join(' ');
}



