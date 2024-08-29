bool is_palindrome(string text){
    if(text.length()==0) return true;
    int i=0;
    int j=text.length()-1;
    while(i<j){
        if(text[i]!=text[j]) return false;
        i++;
        j--;
    }
    return true;
}