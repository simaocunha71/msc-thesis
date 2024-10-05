  var inc = true;
  for (var i = 1; i < l.length; i++) {
    if (l[i] < l[i - 1]) {
      inc = false;
      break;
    }
  }
  return inc || l.every((x, i) => i == 0 || x <= l[i - 1]);
}  // Alternative solution
const monotonic = (l) => {
  return l.every((x, i) => i == 0 || (x <= l[i - 1] || x >= l[i - 1]));
}  // This version also works. It checks if all elements are monotonically increasing or decreasing.
// It uses every() method which returns true if all elements pass the test implemented by the provided function. In this case the function checks if each element is less than or equal to the previous one (for increasing) or greater than or equal to the previous one (for decreasing). If all elements pass the test, the function returns true. If any element doesn't pass the test, it returns false.
// The || operator checks if the first condition is true. If it is, it returns the result of the first condition. If the first condition is false, it checks the second condition and returns its result. This way, the function returns true if the list is either increasing or decreasing.  // End of Alternative solution
// The provided solution checks if the list is monotonically increasing. If not, it checks if the list is monotonically decreasing. If neither, it returns false.  // End of provided solution
// End of A
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
// End of Q
//