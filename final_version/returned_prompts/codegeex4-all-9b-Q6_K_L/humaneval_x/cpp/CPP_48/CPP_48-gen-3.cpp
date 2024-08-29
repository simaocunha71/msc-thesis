bool is_palindrome(string text){
    int len = text.length();
    int i;
    for(i=0;i<len/2;i++){
        if(text[i]!=text[len-i-1]){
            return false;
        }
    }
    return true;
}
