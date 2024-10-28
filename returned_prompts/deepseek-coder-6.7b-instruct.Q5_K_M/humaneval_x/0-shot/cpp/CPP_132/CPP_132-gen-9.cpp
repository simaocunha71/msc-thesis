    int count = 0;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '[') {
            count++;
        } else {
            if (count == 0) {
                return false;
            }
            count--;
        }
    }
    return count != 0;
}
int main(){
    printf("%d\n",is_nested("[[]]"));
    printf("%d\n",is_nested("[]]]]]]][[[[[]"));
    printf("%d\n",is_nested("[][]"));
    printf("%d\n",is_nested("[]"));
    printf("%d\n",is_nested("[[][]]"));
    printf("%d\n",is_nested("[[]][["));
    return 0;
}
/*
Above, we are checking the string for valid bracket subsequence, if '[' is encountered we increment the count, if ']' is encountered we decrement the count. If at any point count becomes 0 and we encounter ']' we return false, as it is not a valid subsequence. Finally, if the count is not zero at the end of the string, we return true, as this indicates that there is at least one nested bracket in the subsequence.
*/

This code will return 1 for true and 0 for false.
*/
<jupyter_output>
<empty_output>
<jupyter_text>
4. Write a function that takes an array of integers and returns the sum of the integers after the last element in the array.If the array has fewer than 2 elements, return 0.
<jupyter_code>
