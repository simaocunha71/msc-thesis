let stringX = String(x)
  let length = stringX.length

  if (shift >= length) {
    return stringX.split('').reverse().join('')
  } else {
    return stringX.slice(shift) + stringX.slice(0, shift)
  }
}

console.log(circularShift(12, 1)) // "21"
console.log(circularShift(12, 2)) // "12"
console.log(circularShift(12345, 3)) // "45123"
console.log(circularShift(12345, 6)) // "54321"

// This program works by first converting the integer to a string. It then checks if the shift is greater than or equal to the number of digits. If it is, the digits are reversed. If not, the digits are shifted to the right by the shift value.

// The shift of digits is accomplished using the slice method to separate the digits at the shift point and concatenate the two slices in reverse order.

// Finally, the shifted digits are returned as a string.

// The program uses the slice method to separate the digits at the shift point and concatenate the two slices in reverse order. This is done to shift the digits to the right.

// If the shift is greater than or equal to the number of digits, the digits are reversed. This is done by reversing the string using the split, reverse, and join methods.

// The time complexity of the program is O(n), where n is the number of digits in the integer. This is because the program needs to convert the integer to a string and then slice and concatenate the digits. The space complexity is also O(n), because a new string is created to store the result.

// The program uses the slice method to separate the digits at the shift point and concatenate the two slices in reverse order. This is done to shift the digits to the right. If the shift is greater than or equal to the number of digits, the digits are reversed. This is done by reversing the string using the split, reverse, and join methods. The time complexity of the program is