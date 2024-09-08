/*my code*/
char x=txt[txt.length()-1];
if(x==' '){
    return false;
}
if(isalpha(x)){
    return true;
}
if(isalnum(x)){
    return false;
}
if(isdigit(x)){
    return false;
}
if(!isalpha(x)){
    return false;
}
return false;
}
int main(){
    string s;
    scanf("%[^\n]%*c",&s);
    check_if_last_char_is_a_letter(s);
    return 0;
}
