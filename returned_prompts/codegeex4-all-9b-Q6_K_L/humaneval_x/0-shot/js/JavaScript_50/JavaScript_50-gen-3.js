The code is correct.

The `encodeShift` function shifts every character by 5 in the alphabet. It works by splitting the input string into an array of characters, then mapping over each character and converting it to its ASCII code using `charCodeAt`. It adds 5 to the ASCII code, subtracts the ASCII code of "a", takes the modulus of 26 to wrap around the alphabet, and then adds the ASCII code of "a" back. Finally, it joins the array back into a string.

The `decodeShift` function does the opposite of `encodeShift`. It subtracts 5 from the ASCII code, adds the ASCII code of "a", takes the modulus of 26 to wrap around the alphabet, and then adds the ASCII code of "a" back. Finally, it joins the array back into a string.