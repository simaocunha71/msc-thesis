    int i;
    int counter=0;
    string temp=str;
    sort(temp.begin(),temp.end());

    for (i=0;i<temp.length();i++)
    {
        if (temp[i]!=temp[i+1])
        counter+=1;
    }
    return counter;
}

