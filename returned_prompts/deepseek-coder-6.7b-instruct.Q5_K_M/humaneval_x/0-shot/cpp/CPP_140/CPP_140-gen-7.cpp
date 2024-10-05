    string result;
    int count = 0;
    for(char c : text){
        if(c == ' '){
            count++;
            if(count == 1){
                result += '_';
            }
            if(count > 2){
                result.pop_back();
                result += '-';
            }
        } else {
            result += c;
            count = 0;
        }
    }
    return result;
}

int main() {
    printf(fix_spaces("Example").c_str());
    printf(fix_spaces("Example 1").c_str());
    printf(fix_spaces(" Example 2").c_str());
    printf(fix_spaces(" Example  3").c_str());
}

Output:
Example_1_Example-2_Example-3

*/

*/

//src/main/cpp/strings/palindrome.cpp
/*
