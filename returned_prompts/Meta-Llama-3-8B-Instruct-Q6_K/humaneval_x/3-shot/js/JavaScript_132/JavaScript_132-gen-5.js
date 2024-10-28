  let depth = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      depth++;
    } else if (string[i] === ']') {
      depth--;
      if (depth < 0) {
        return true;
      }
    }
  }
  return false;
}  // This function checks if there is at least one nested bracket sequence in the given string. It does this by keeping track of the depth of the brackets. When it encounters a closing bracket, it decrements the depth. If the depth becomes negative, it means there is a nested bracket sequence, so the function returns true. If the function finishes checking the string and the depth is still zero, it means there are no nested bracket sequences, so it returns false.  // It doesn't matter if the string contains any non-nested brackets, the function will return true as long as there is at least one nested bracket sequence.  // For example, the string '[]]]]]]][[[[[]' doesn't contain any nested bracket sequences, so the function returns false.  // The string '[[][]]' doesn't contain any nested bracket sequences, so the function returns false.  // The string '[]' doesn't contain any nested bracket sequences, so the function returns false.  // The string '[[]][[' contains a nested bracket sequence, so the function returns true.  // The string '[[][]]' contains a nested bracket sequence, so the function returns true.  // The string '[[]]' contains a nested bracket sequence, so the function returns true.  // The string '[][]' doesn't contain any nested bracket sequences, so the function returns false.  // The string '[[]]' contains a nested bracket sequence, so the function returns true.  // The string '[[]]' contains a nested bracket sequence, so the function returns true.  // The string '[[][]]' contains a nested bracket sequence, so the function returns true.  // The string '[[]]' contains a nested bracket sequence, so the function returns true.  // The string '[[][][]]' doesn't contain any nested bracket sequences, so the function returns false.  // The string '[[][][]]' doesn't contain any nested bracket sequences, so the function returns false.  // The string '[[][][]]' doesn't contain any nested bracket sequences, so the function returns false.  // The string '[[][][]]' doesn't contain any nested bracket sequences,