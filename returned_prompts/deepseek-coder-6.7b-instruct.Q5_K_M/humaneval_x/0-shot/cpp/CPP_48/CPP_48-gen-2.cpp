    int start = 0;
    int end = text.length() - 1;
    while (start < end){
        if (text[start] != text[end]){
            return false;
        }
        start++;
        end--;
    }
    return true;
}
int main(){
    string text;
    printf("Enter the string: ");
    getline(cin, text);
    if(is_palindrome(text)){
        printf("true\n");
    }
    else{
        printf("false\n");
    }
    return 0;
}
*/

//Problems/C++/4.cpp
/*
