    int count=0;
    for(auto str: lst)
    for(auto ch: str)
    {
        if(ch=='(')
            count++;
        else if(ch==')' && count==0)
            return "No";
        else if(ch==')')
            count--;
    }
    return count==0 ? "Yes" : "No";
}


