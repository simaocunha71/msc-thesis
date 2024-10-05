    int len = str.size();
    int i = 0, j = len-1;
    while(i<j){
        if(str[i] != str[j])
            break;
        i++;
        j--;
    }
    string palindrome_suffix = str.substr(i,j-i+1);
    int palindrome_len = palindrome_suffix.size();
    string palindrome_prefix = str.substr(0,i);
    for(int i = palindrome_len-1;i>=0;i--)
        str.insert(len,palindrome_prefix);
    return str.substr(0,len+palindrome_len);
}




