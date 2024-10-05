    for(int i = 0; i < text.size(); i++){
        if(text[i] == ' '){
            if(i+1 < text.size() && text[i+1] == ' '){
                text.replace(i, 2, "-");
            }
            else{
                text[i] = '_';
            }
        }
    }
    return text;
}

int main(){
    string text1 = "Example";
    string text2 = "Example 1";
    string text3 = " Example 2";
    string text4 = " Example  3";
    
    printf("%s\n", fix_spaces(text1).c_str());
    printf("%s\n", fix_spaces(text2).c_str());
    printf("%s\n", fix_spaces(text3).c_str());
    printf("%s\n", fix_spaces(text4).c_str());
}
*/

