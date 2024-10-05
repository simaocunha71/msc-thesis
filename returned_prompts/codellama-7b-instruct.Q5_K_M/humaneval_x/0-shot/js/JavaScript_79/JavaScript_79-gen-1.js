/*
  let binary = '';
  while (decimal > 0) {
    const remainder = decimal % 2;
    binary = remainder + binary;
    decimal = Math.floor(decimal / 2);
  }
  return 'db' + binary + 'db';
}
*/

B:
/*
const decimalToBinary = (decimal) => {
  let binary = '';
  while (decimal > 0) {
    binary = (decimal % 2) + binary;
    decimal = Math.floor(decimal / 2);
  }
  return 'db' + binary + 'db';
}
*/

C:
/*
const decimalToBinary = (decimal) => {
  let binary = '';
  while (decimal > 0) {
    binary = decimal % 2 + binary;
    decimal = Math.floor(decimal / 2);
  }
  return 'db' + binary + 'db';
}
*/

D:
/*
const decimalToBinary = (decimal) => {
  let binary = '';
  while (decimal > 0) {
    binary = (decimal % 2) + binary;
    decimal = Math.floor(decimal / 2);
  }
  return 'db' + binary + 'db';
}
*/

E:
/*
const decimalToBinary = (decimal) => {
  let binary = '';
  while (decimal > 0) {
    binary = decimal % 2 + binary;
    decimal = Math.floor(decimal / 2);
  }
  return 'db' + binary + 'db';
}
*/
