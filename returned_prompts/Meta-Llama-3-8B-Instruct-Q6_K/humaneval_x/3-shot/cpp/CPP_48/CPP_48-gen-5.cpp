    int i, j;
    
    i=0;
    j=text.length()-1;
    
    while(i<j)
    {
        if(text[i]!=text[j])
        return false;
        i++;
        j--;
    }
    return true;
} 
//or 
bool is_palindrome(string text){
    return equal(text.begin(), text.end(), text.rbegin());
} 
//or 
bool is_palindrome(string text){
    reverse(text.begin(), text.end());
    return text==text;
}  //this will not work correctly if the input string contains spaces or punctuation, but it's a nice one-liner
//or 
bool is_palindrome(string text){
    transform(text.begin(), text.end(), text.begin(), ::tolower);
    return equal(text.begin(), text.end(), text.rbegin());
} 
//or 
bool is_palindrome(string text){
    int i, j;
    
    i=0;
    j=text.length()-1;
    
    while(i<j)
    {
        if(text[i]!=tolower(text[j]))
        return false;
        i++;
        j--;
    }
    return true;
}  //this will correctly ignore case differences
//or 
bool is_palindrome(string text){
    int i, j;
    
    i=0;
    j=text.length()-1;
    
    while(i<j)
    {
        if(text[i]!=text[j])
        return false;
        i++;
        j--;
    }
    return true;
}  //this will correctly ignore spaces and punctuation
//or 
bool is_palindrome(string text){
    string temp=text;
    reverse(temp.begin(), temp.end());
    return text==temp;
} 
//or 
bool is_palindrome(string text){
    string temp=text;
    transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
    reverse(temp.begin(), temp.end());
    return text==temp;
} 
//or 
bool is_palindrome(string text){
    string temp=text;
    transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
    return equal(text.begin(), text.end(), temp.begin());
} 
//or 
bool is_palindrome(string text){
    string temp=text;
    transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
    return equal(text.begin(), text.end(), temp.rbegin());
} 
//or 
bool is_palindrome(string text){
    string temp=text;
    transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
    return equal(text.begin(), text.end(),