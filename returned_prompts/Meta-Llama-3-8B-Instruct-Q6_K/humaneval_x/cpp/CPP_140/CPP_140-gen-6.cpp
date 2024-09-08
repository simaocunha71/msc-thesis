    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            if(i > 0 && text[i-1] == ' '){
                // if it's the last space, add - at the end
                if(i == text.length()-1) text += '-';
                else text.insert(i+1, "-");
                i++;
            }
            else text.replace(i, 1, "_");
        }
    }
    return text;
}

int main(){
    string test_cases[] = {"Example", "Example 1", " Example 2", " Example   3"};
    for(int i = 0; i < sizeof(test_cases)/sizeof(test_cases[0]); i++){
        cout << test_cases[i] << " == " << fix_spaces(test_cases[i]) << endl;
    }
    return 0;
}

