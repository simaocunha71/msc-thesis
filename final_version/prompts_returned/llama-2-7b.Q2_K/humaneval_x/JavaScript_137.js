/*
  Create a function that takes integers, floats, or strings representing
  real numbers, and returns the larger variable in its given variable type.
  Return null if the values are equal.
  Note: If a real number is represented as a string, the floating point might be . or ,

  compareOne(1, 2.5) ➞ 2.5
  compareOne(1, "2,3") ➞ "2,3"
  compareOne("5,1", "6") ➞ "6"
  compareOne("1", 1) ➞ null
  */
const compareOne = (a, b) => {
    if (!isNaN(parseFloat(b))) return parseFloat(b) > 0 ? parseFloat(b) : parseFloat(a);
    const [num, dec] = stringToNumber(b);
    let numB;
    try {
      numB = parseFloat(dec);
    } catch (err) { return null; }
    if (!isNaN(parseFloat(num))) return parseFloat(a) > 0 ? parseFloat(a) : parseFloat(b);
    const [num, dec2] = stringToNumber(num);
    let numA;
    try {
      numA = parseFloat(dec2);
    } catch (err) { return null; }
    if (!isNaN(parseFloat(a))) return parseFloat(a) > 0 ? parseFloat(a) : parseFloat(b);
    let cmp;
    try {
      cmp = numA < numB && parseFloat(dec2) >= parseFloat(dec) ? -1 :
        (numA == numB && strcmp(dec, dec2) <= 0) ? 0 : 1;
    } catch (err) { return null; }
    if (!isNaN(parseFloat(a))) return cmp > 0 ? parseFloat(b) : parseFloat(a);
    const [num, rest] = stringToNumber(dec + "-" + dec2);
    let rt;
    try {
      rt = (rest == "e-"+dec+"."+rest && parseFloat(dec2