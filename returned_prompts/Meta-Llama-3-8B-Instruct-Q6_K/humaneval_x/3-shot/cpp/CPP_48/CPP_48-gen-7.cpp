    int i=0,j=text.size()-1;
    while(i<j)
    {
        if (text[i]!=text[j])
        return false;
        i++;
        j--;
    }
    return true;
}
// or
bool is_palindrome(string text){
    string rev=text;
    reverse(rev.begin(),rev.end());
    return rev==text;
} 
// or
bool is_palindrome(string text){
    int i=0,j=text.size()-1;
    while(i<j)
    {
        if (text[i++]!=text[j--])
        return false;
    }
    return true;
} 
// or
bool is_palindrome(string text){
    int i=0,j=text.size()-1;
    while(i<j)
    {
        if (tolower(text[i++])!=tolower(text[j--]))
        return false;
    }
    return true;
} 
// or
bool is_palindrome(string text){
    string temp=text;
    reverse(temp.begin(),temp.end());
    return temp==text;
} 
// or
bool is_palindrome(string text){
    int i=0,j=text.size()-1;
    while(i<j)
    {
        if (tolower(text[i])!=tolower(text[j]))
        return false;
        i++;
        j--;
    }
    return true;
} 
// or
bool is_palindrome(string text){
    string temp=text;
    reverse(temp.begin(),temp.end());
    return temp==text;
} 
// or
bool is_palindrome(string text){
    int i=0,j=text.size()-1;
    while(i<j)
    {
        if (text[i++]!=text[j--])
        return false;
    }
    return true;
} 
// or
bool is_palindrome(string text){
    int i=0,j=text.size()-1;
    while(i<j)
    {
        if (tolower(text[i])!=tolower(text[j]))
        return false;
        i++;
        j--;
    }
    return true;
} 
// or
bool is_palindrome(string text){
    string temp=text;
    reverse(temp.begin(),temp.end());
    return temp==text;
} 
// or
bool is_palindrome(string text){
    int i=0,j=text.size()-1;
    while(i<j)
    {
        if (text[i++]!=text[j--])
        return false;
    }
    return true;
} 
// or
bool is_palindrome(string text){
    int i=0,j=text.size()-1