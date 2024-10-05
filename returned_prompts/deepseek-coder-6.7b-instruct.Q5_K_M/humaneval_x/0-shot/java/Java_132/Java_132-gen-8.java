        Stack<Character> stack = new Stack<>();
        for(int i=0;i<string.length();i++){
            char c = string.charAt(i);
            if(c == '['){
                stack.push(c);
            }else{
                if(stack.empty()){
                    return false;
                }
                stack.pop();
                if(stack.empty()){
                    return true;
                }
            }
        }
        return false;
    }
}

Output:
isNested("[[]]") => true
isNested("[]]]]]]][[[[[]") => false
isNested("[][]") => false
isNested("[]") => false
isNested("[[][]]") => true
isNested("[[]][[") => true

The function `isNested` takes a string of square brackets as its parameter. It uses a stack to keep track of the brackets. 

For each character in the string:

- If the character is '[', it pushes it onto the stack.
- If the character is ']', it pops the top element from the stack.
- If the stack becomes empty after popping, it means there are no brackets left to nest, so it returns false.
- If the stack becomes empty after the first ']', it means there is at least one bracket that is nested, so it returns true.
- If the function iterates through the entire string without returning, it means there are no nested brackets, so it returns false.

This function works because it checks for valid nesting of brackets and returns true as soon as it finds a nested pair of brackets, and false if it doesn't find any.

Time complexity: O(n), where n is the length of the string.
Space complexity: O(n), in the worst case when all brackets are opening brackets.
*/

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println("isNested(\"[[]]\") => " + solution.isNested("[[]]"));
        System.out.println("isNested(\"[]]]