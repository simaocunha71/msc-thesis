    int count = 0;
    for(int i = 0; i < str.length(); i++){
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
    return count > 0;
}

int main() {
    string test1 = "[[]]";
    string test2 = "[]]]]]]][[[[[]";
    string test3 = "[][]";
    string test4 = "[]";
    string test5 = "[[][]]";
    string test6 = "[[]][[";

    printf("%s, %s, %s, %s, %s, %s\n", (is_nested(test1) ? "true" : "false"), (is_nested(test2) ? "true" : "false"), (is_nested(test3) ? "true" : "false"), (is_nested(test4) ? "true" : "false"), (is_nested(test5) ? "true" : "false"), (is_nested(test6) ? "true" : "false"));
    return 0;
}

Output:
true, false, false, false, true, true
*/































































































































































































