Here is the solution for the problem:
```
const encrypt = (s) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const shiftedAlphabet = alphabet.slice(2 * 2, alphabet.length) + alphabet.slice(0, 2 * 2);
  return s.split('').map(c => {
    if (c === ' ') return ' ';
    const index = alphabet.indexOf(c.toLowerCase());
    return index === -1 ? c : shiftedAlphabet[index % shiftedAlphabet.length].toUpperCase() === c ? shiftedAlphabet[index % shiftedAlphabet.length].toLowerCase() : shiftedAlphabet[index % shiftedAlphabet.length].toUpperCase();
  }).join('');
};
```
Here's an explanation of the code:

1. We define the alphabet and create a shifted alphabet by slicing the original alphabet and concatenating it with the beginning of the alphabet.
2. We split the input string into individual characters.
3. We map over the characters, checking if each character is a space. If it is, we return the space.
4. If the character is a letter, we find its index in the original alphabet.
5. We check if the index is valid (i.e., not -1). If it's not, we return the original character.
6. If the index is valid, we calculate the new index in the shifted alphabet using the modulo operator. This ensures that the rotation wraps around.
7. We uppercase or lowercase the character based on whether the original character was uppercase or lowercase.
8. We join the encrypted characters back into a string and return it.

You can test the function with the examples provided in the problem statement to see that it produces the expected output.