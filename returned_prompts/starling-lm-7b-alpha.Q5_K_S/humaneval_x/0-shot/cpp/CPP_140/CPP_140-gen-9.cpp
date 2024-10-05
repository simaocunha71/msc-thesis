    int len = text.length();
    if(len == 0) return "";

    int i = 0;
    while(i < len && text[i] == ' ') i++;
    if(i == len) return "_";

    int j = i;
    while(j < len){
        if(text[i] == ' ' && text[j] == ' '){
            while(j < len && text[j] == ' '){ j++; }
            i = j - 1;
            if(i + 1 < len && text[i + 1] == ' '){
                text[i + 1] = '-';
            }
        }else{
            if(text[i] == ' '){
                text[i] = '_';
                i++;
                while(i < j && text[i] == ' '){ i++; }
            }else{
                i++;
                j++;
            }
        }
    }

    return text;
}

int main(){
    printf("%s\n", fix_spaces("Example").c_str());
    printf("%s\n", fix_spaces("Example 1").c_str());
    printf("%s\n", fix_spaces(" Example 2").c_str());
    printf("%s\n", fix_spaces(" Example   3").c_str());
}


*/






/*
















*/






















































































































































