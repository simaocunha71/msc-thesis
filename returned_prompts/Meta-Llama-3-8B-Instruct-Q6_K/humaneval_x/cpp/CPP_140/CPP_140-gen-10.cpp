    string s = "";
    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            if(s.length() > 0 && s[s.length()-1] == ' '){
                s += "-";
            }else{
                s += "_";
            }
        }else{
            s += text[i];
        }
    }
    return s;
}
int main(){
    string text = " Example   3";
    string res = fix_spaces(text);
    printf("Result is: %s\n",res.c_str());
    return 0;
}

