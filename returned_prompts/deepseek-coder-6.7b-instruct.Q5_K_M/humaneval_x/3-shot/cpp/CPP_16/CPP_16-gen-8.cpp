    vector<int> count(256,0);
    int result=0;
    for  (int i=0; str[i]; i++)
    {
        if  (count[tolower(str[i])]==0 && isalpha(str[i]))
        {
            result++;
            count[tolower(str[i])]=1;
        }
    }
    return result;
}

