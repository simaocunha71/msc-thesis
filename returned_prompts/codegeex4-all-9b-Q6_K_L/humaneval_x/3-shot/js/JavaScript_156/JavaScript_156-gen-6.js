  let roman = '';
  while (number >= 1000) {
    roman += 'm';
    number -= 1000;
  }
  while (number >= 500) {
    roman += 'd';
    number -= 500;
  }
  while (number >= 100) {
    roman += 'c';
    number -= 100;
  }
  while (number >= 50) {
    roman += 'l';
    number -= 50;
  }
  while (number >= 10) {
    roman += 'x';
    number -= 10;
  }
  while (number >= 5) {
    roman += 'v';
    number -= 5;
  }
  while (number >= 1) {
    roman += 'i';
    number -= 1;
  }
  return roman;
}