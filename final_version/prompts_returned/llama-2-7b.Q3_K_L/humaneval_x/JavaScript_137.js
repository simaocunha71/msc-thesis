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
    if (typeof a === 'string' && typeof b === 'number') { // convert to number
        const numResult = parseFloat(b); // get float result
        let stringResult;
        try { // check for errors when converting to number
            stringResult = parseFloat(a);
        } catch (e) {} // if error convert back to string
        return (stringResult === a && stringResult === numResult ? b : numResult > stringResult ? b : stringResult);
    } else if (typeof a === 'number' && typeof b === 'string') { // convert to string
        const strResult = parseFloat(b) + ','; // get float result
        let numResult;
        try {
            numResult = parseFloat(a);
        } catch (e) {}
        return (numResult === a && numResult === strResult ? b : strResult > numResult ? b : numResult);
    } else if (typeof a === 'string' && typeof b === 'string') { // compare strings
      const min = Math.min(a.length, b.length);
      for (let i = 0; i < min; ++i) {
          let x = parseFloat(a[i]);
          let y = parseFloat(b[i]);
        }
    } else if (typeof a === 'string' && typeof b === 'number') { // compare number and string - need to do this first since .35 vs "1,3" is technically higher than 1.6
      const min = Math.min(a.length, b);