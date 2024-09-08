    int i = 0;
    int count = 0;
    string result = "";
    
    while(i < text.length()){
        if(text[i] == ' '){
            if(count == 0){
                result += '_';
                count++;
            }
            else if(count == 1){
                result += '-';
                count++;
            }
            else{
                count = 0;
            }
        }
        else{
            for(int j = 0; j < count; j++){
                result += '_';
            }
            count = 0;
            result += text[i];
        }
        i++;
    }
    return result;
}

int main(){
    string s1 = "Example";
    string s2 = "Example 1";
    string s3 = " Example 2";
    string s4 = " Example   3";

    cout << fix_spaces(s1) << endl;
    cout << fix_spaces(s2) << endl;
    cout << fix_spaces(s3) << endl;
    cout << fix_spaces(s4) << endl;

    return 0;
}

B:
    #include <iostream>
    #include <string>
    #include <algorithm>

    std::string fix_spaces(const std::string& text) {
        std::string result;
        bool prevSpace = false;

        for (char c : text) {
            if (c == ' ') {
                if (prevSpace) {
                    result += '-';
                    prevSpace = false;
                } else {
                    result += '_';
                    prevSpace = true;
                }
            } else {
                result += c;
                prevSpace = false;
            }
        }
        return result;
    }

    int main() {
        std::string s1 = "Example";
        std::string s2 = "Example 1";
        std::string s3 = " Example 2";
        std::string s4 = " Example   3";

        std::cout << fix_spaces(s1) << std::endl;
        std::cout << fix_spaces(s2) << std::endl;
        std::cout << fix_spaces(s3) << std::endl;
        std::cout << fix_spaces(s4) << std::endl;

        return 0;
    }C:
    #include <iostream>
    #include <string>
    #include <algorithm>

    std::string fix_spaces(const std::string& text) {
        std::string result;
        for (char c : text