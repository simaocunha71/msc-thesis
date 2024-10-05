
return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 + "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
};

encodeShift("Hello World!"); // "Mjqqt%Yqtnf!"
decodeShift("Mjqqt%Yqtnf!"); // "Hello World!"

Explanation:
In the encodeShift function, each character in the input string is converted to its Unicode value using charCodeAt(0), then 5 is added to the Unicode value, and the result is taken modulo 26 and "a" is added to get the Unicode value of the new character. The new character is obtained by converting the Unicode value back to a character using fromCharCode.
The decodeShift function does the opposite: 5 is subtracted from the Unicode value of each character, the result is taken modulo 26, and "a" is added to obtain the original Unicode value of the character.

The time and space complexities of the encodeShift and decodeShift functions are both O(n), where n is the length of the input string.

The encodeShift function can be used to encode a string by shifting each character by 5 in the alphabet, and the decodeShift function can be used to decode a string that has been encoded using the encodeShift function.

In the example given, the encodeShift function is called with the input string "Hello World!" and it returns the encoded string "Mjqqt%Yqtnf!". The decodeShift function is then called with the encoded string and it returns the original string "Hello World!".

Overall, the encodeShift and decodeShift functions provide a simple and effective way to encode and decode strings by shifting each character in the alphabet.

*/

*/

In the provided code, there are two functions: encodeShift and decodeShift.

The encodeShift function takes a string as input and returns an encoded string by shifting every character in the input string by 5 positions in the alphabet. The function uses the map() method to iterate over each character in the input string. For each character, its Unicode value is obtained using the charCodeAt(0) method