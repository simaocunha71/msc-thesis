    int i = 0;
    while(i < text.length()) {
        if(text[i] == ' '){
            if(text[i+1] == ' '){
                if(text[i+2] == ' '){
                    text = text.substr(0, i) + "-" + text.substr(i+2);
                    i = 0;
                    continue;
                }
                text = text.substr(0, i) + "_" + text.substr(i+1);
                i = 0;
                continue;
            }
            text = text.substr(0, i) + "_" + text.substr(i+1);
            i = 0;
            continue;
        }
        i++;
    }
    return text;
}

int main() {
    string s = " Example   3";
    string result = fix_spaces(s);
    printf("%s\n", result.c_str());
    return 0;
}

