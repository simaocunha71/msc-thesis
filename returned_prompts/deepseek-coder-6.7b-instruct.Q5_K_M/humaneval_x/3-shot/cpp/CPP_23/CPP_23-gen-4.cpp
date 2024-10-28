    int start=0;
    int end=str.length()-1;
    while(start<end){
        while (start < end && !isalnum(str[start]))
            start++;
        while (start < end && !isalnum(str[end]))
            end--;
        if (tolower(str[start]) != tolower(str[end]))
            return false;
        start++;
        end--;
    }
    return true;
}


