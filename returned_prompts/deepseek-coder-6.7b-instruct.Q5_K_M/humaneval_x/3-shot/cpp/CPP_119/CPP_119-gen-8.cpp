    int open=0, close=0;
    for(string s: lst)
    {
        for(char c: s)
        {
            if(c=='(') open++;
            else if(c==')')
            {
                if(open>0) open--;
                else close++;
            }
        }
    }

    if(open==close) return "Yes";
    return "No";
}



