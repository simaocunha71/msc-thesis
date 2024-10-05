    map<char,int> output;
    string current;
    int count=0;
    int i;
    for (i=0;i<test.length();i++)
    {
        current=test[i];
        if (output.find(current)!=output.end())
        {
            count=output[current]+1;
            output[current]=count;
        }
        if (output.find(current)==output.end())
        {
            output[current]=1;
        }
    }
    return output;
}


