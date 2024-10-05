const sameChars = (s0, s1) => {
  // convert strings to arrays of characters
  const s0Arr = s0.split('');
  const s1Arr = s1.split('');
  // check if arrays have the same length
  if (s0Arr.length !== s1Arr.length) {
    return false;
  }
  // loop through the arrays
  for (let i = 0; i < s0Arr.length; i++) {
    // if any array has the same character as the other
    if (s0Arr[i] !== s1Arr[i]) {
      return false;
    }
  }
  return true;
}

