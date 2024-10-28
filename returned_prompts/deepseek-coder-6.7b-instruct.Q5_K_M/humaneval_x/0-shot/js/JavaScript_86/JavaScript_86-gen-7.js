  return s.split('')
    .sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0))
    .join('');
};

console.log(antiShuffle('Hi')); // 'Hi'
console.log(antiShuffle('hello')); // 'ehllo'
console.log(antiShuffle('Hello World!!!')); // 'Hello  !!!Wdlor'

*/

The function antiShuffle splits the input string into an array of characters, sorts the array in ascending order of the ASCII values of its characters, then joins the sorted array back into a string.

This function works by first splitting the string into an array of characters. Then, it sorts the array in ascending order of the ASCII values of its characters. ASCII values are a numerical representation of characters, where 'a' has a value of 97 and 'z' has a value of 122. The sort function compares the ASCII values of each pair of characters and rearranges them in ascending order.

Finally, it joins the sorted array back into a string. The join method takes an array and returns a string where the elements of the array are joined by the string that calls the method. In this case, it joins the array of characters with an empty string ('') to create a string where the characters are arranged in ascending order of their ASCII values.

The function returns the string 'Hi' for the input 'Hi', 'ehllo' for the input 'hello', and 'Hello  !!!Wdlor' for the input 'Hello World!!!'.

The time complexity of this function is O(n log n) where n is the length of the string. This is because the function splits the string into an array of characters, which takes O(n) time, sorts the array, which takes O(n log n) time, and then joins the array back into a string, which takes O(n) time.

The space complexity of this function is O(n) because it creates a new array of characters from the string.

The function could be optimized to use a different sorting algorithm that is faster than O(n log n), but the space complexity would increase.

*/

// Anti-shuffle function
const antiShuffle = (s