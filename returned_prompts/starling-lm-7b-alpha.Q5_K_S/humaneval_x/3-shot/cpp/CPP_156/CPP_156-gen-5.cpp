    vector<string> Roman={
        {"i","ii","iii"},
        {"iv"},
        {"v","vi","vii"},
        {"viii"},
        {"ix"},
        {"x"},
        {"xl"},
        {"l"},
        {"lx"},
        {"lxx"},
        {"lxxxi"},
        {"xc"},
        {"c"},
        {"cd"},
        {"d"},
        {"dcc"},
        {"dc"},
        {"cm"},
        {"m"},
        {"mm"},
        {"mml"},
        {"mmm"},
    };
    string result;
    int i,j;

    for (i=Roman.size()-1;i>=0;i--)
    {
        for (j=0;j<Roman[i].size();j++)
        {
            while (number>=i*Roman[i][j][0]-'0')
            {
                result+=Roman[i][j];
                number-=i*Roman[i][j]-'0';
            }
        }
    }
    return result;
}


