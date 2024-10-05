    int count = 0;
    for(char c: brackets){
        if(c == '(') count++;
        else if(c == ')') count--;
        if(count < 0) return false; //If we encounter a closing bracket before opening bracket.
    }

B:
    return count == 0; //If there are unmatched opening brackets.
}

int main() {
    printf("%s\n", correct_bracketing("(") ? "true" : "false");
    printf("%s\n", correct_bracketing("()") ? "true" : "false");
    printf("%s\n", correct_bracketing("(()())") ? "true" : "false");
    printf("%s\n", correct_bracketing(")(()") ? "true" : "false");
}

This solution works by counting the number of opening brackets (incrementing count) and closing brackets (decrementing count). If at any point count is negative, we know there is a closing bracket before an opening bracket, so we return false. If count is not zero at the end, we know there are unmatched opening brackets, so we return false. If none of these cases is true, we return true.
*/

int main() {
    printf("%s\n", correct_bracketing("(") ? "true" : "false");
    printf("%s\n