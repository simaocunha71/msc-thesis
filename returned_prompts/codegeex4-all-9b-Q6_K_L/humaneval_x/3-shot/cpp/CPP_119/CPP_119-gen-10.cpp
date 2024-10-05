    int i=0;
    string result;
    int left=0;
    int right=0;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]=="(")
        left+=1;
        if (lst[i]==")")
        right+=1;
    }
    if (left==right)
    result="Yes";
    else
    result="No";
    return result;
}

