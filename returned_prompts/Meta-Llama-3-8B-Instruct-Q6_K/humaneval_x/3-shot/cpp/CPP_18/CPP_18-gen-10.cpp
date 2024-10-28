    int count=0;
    size_t pos=0;
    while ((pos=str.find(substring,pos))!=string::npos){
        count++;
        pos+=substring.length();
    }
    return count;
}  // this function is case sensitive. If you want to make it case insensitive, you can convert both strings to lower case before the search.