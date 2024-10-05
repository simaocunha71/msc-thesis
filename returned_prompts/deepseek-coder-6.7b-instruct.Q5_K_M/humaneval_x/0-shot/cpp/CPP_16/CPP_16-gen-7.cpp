We use a vector of size 256 to store the frequency of each character in the string. We initialize all the elements of the vector to 0. The ASCII value of a character is used as the index of the vector. 

Then we iterate through the string. For each character, we convert it to lowercase (if it is uppercase) and increment the count of that character in the vector.

Finally, we count the number of elements in the vector that have a value of 1 (which means the character has occurred at least once). This is the number of distinct characters in the string.

The time complexity of this solution is O(n), where n is the length of the string.

The space complexity is also O(n) because we use a vector of size 256 to store the frequency of each character in the string.

This solution assumes that the string only contains ASCII characters. If the string can contain Unicode characters, the solution would need to be modified to use a different data structure to store the frequency of each character.

The function count_distinct_characters takes a string as input and returns the number of distinct characters in the string.
*/

