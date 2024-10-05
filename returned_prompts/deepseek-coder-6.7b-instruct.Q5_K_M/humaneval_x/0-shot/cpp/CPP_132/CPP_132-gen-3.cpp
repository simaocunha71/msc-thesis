    int count = 0;
    for(int i = 0; i < str.size(); i++){
        if(str[i] == '['){
            count++;
        }
        else if(str[i] == ']'){
            count--;
            if(count < 0){
                return false;
            }
        }
    }
    return (count > 0);
}

int main() {
    printf("%d\n",is_nested("[[]]"));
    printf("%d\n",is_nested("[]]]]]]][[[[[]"));
    printf("%d\n",is_nested("[][]"));
    printf("%d\n",is_nested("[]"));
    printf("%d\n",is_nested("[[][]]"));
    printf("%d\n",is_nested("[[]][["));
    return 0;
}

This program works by maintaining a count of the number of open brackets that are left unclosed. If it ever encounters a closed bracket and the count is zero, then there is no open bracket left to close it, so it returns false. If it finishes counting the brackets and there are still some left unclosed, then it returns true.
This program assumes that the string only contains square brackets and that it is well-formed. If there can be other characters in the string, then it should be updated to skip those characters.
*/


















































































































































































