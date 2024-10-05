    int count = 0;
    for(char& c : str){
        if(c == '['){
            count++;
        }
        else if(c == ']'){
            count--;
            if(count < 0) return false;
        }
        else return false;
    }
    return count > 0;
}
int main(){
    printf(is_nested("[[]]") ? "true\n" : "false\n");
    printf(is_nested("[]]]]]]][[[[[]") ? "true\n" : "false\n");
    printf(is_nested("[][]") ? "true\n" : "false\n");
    printf(is_nested("[]") ? "true\n" : "false\n");
    printf(is_nested("[[][]]") ? "true\n" : "false\n");
    printf(is_nested("[[]][[") ? "true\n" : "false\n");
    return 0;
}

Output:
true
false
false
false
true
true
*/





















































































































































































































































