
This is a very good collection of interview questions!  I'll give a few suggestions for improvement.
1. Use better variable names.  This makes the code more readable and reduces the likelihood of mistakes.  For example, in hasCloseElements, I would prefer:
const hasCloseElements = (numbers, threshold) => {
  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      if (i != j) {
        const distance = Math.abs(numbers[i] - numbers[j]);
        if (distance < threshold) {
          return true;
        }
      }
    }
  }
  return false;
}

2. Use const and let instead of var.  This makes it clear which variables are constants and which are variables that can be reassigned.
3. Use template literals instead of string concatenation.  This makes the code more readable and reduces the likelihood of mistakes.  For example, in strongestExtension, I would prefer:
const strongestExtension = (class_name, extensions) => {
  let strongest = extensions[0];
  for (const extension of extensions) {
    if (extension.length > strongest.length) {
      strongest = extension;
    } else if (extension.length == strongest.length) {
      let strength = 0;
      for (const c of extension) {
        if (c == c.toUpperCase()) {
          strength += 1;
        } else {
          strength -= 1;
        }
      }
      let strongest_strength = 0;
      for (const c of strongest) {
        if (c == c.toUpperCase()) {
          strongest_strength +=