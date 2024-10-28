
// Use a loop to iterate over the string.
// If the string at the current index is '[', push it to a stack.
// If the string at the current index is ']', pop the element from the stack and check if it is '['.
// If it is not '[', push the current element to the stack.
// After the loop, if the stack is empty, return false. Otherwise, return true.

B:

// Initialize a variable "nested" to false.
// Initialize a stack.
// Iterate over the string.
// If the character is '[', push it to the stack.
// If the character is ']', pop the top element from the stack.
// If the popped element is '[', set "nested" to true and break the loop.
// If the stack is empty, return false.
// If "nested" is still false after the loop, return false.
// Otherwise, return true.

C:

// Initialize a stack.
// Iterate over the string.
// If the character is '[', push it to the stack.
// If the character is ']', pop the top element from the stack.
// If the popped element is not '[', push the character back to the stack.
// If the stack is empty, return false.
// If the stack is not empty, return true.

D:

// Initialize a stack.
// Iterate over the string.
// If the character is '[', push it to the stack.
// If the character is ']', pop the top element from the stack.
// If the popped element is '[', return true.
// If the stack is empty, return false.

E:

// Initialize a stack.
// Iterate over the string.
// If the character is '[', push it to the stack.
// If the character is ']', pop the top element from the stack.
// If the popped element is not '[', push the character back to the stack.
// If the stack is empty, return false.
// If the stack is not empty, return true.

}

*/

// IsNested checks if there is a valid subsequence of brackets where at least one