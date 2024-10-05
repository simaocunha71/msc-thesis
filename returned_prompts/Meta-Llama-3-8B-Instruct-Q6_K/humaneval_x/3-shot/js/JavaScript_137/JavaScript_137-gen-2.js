  if (typeof a === 'string' && typeof b === 'string') {
    a = parseFloat(a.replace(',', ''));
    b = parseFloat(b.replace(',', ''));
  } else if (typeof a === 'string') {
    a = parseFloat(a);
  } else if (typeof b === 'string') {
    b = parseFloat(b);
  }
  if (a > b) {
    return a;
  } else if (a < b) {
    return b;
  } else {
    return null;
  }
}
// Example usage:
console.log(compareOne(1, 2.5)); // 2.5
console.log(compareOne(1, "2,3")); // "2,3"
console.log(compareOne("5,1", "6")); // "6"
console.log(compareOne("1", 1)); // null
// ...and so on.