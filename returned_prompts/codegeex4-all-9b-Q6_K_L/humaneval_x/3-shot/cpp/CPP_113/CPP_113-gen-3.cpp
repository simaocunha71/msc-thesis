    vector<string> all_odd;
    string current_odd;
    map<string,string> m;
    int i,j;
    char chr;
    for (i=0;i<lst.size();i++)
    {
        current_odd="";
        for (j=0;j<lst[i].length();j++)
        {
            chr=lst[i][j];
            if (chr=='1' || chr=='3' || chr=='5' || chr=='7' || chr=='9')
            current_odd+='1';
            else
            current_odd+='0';
        }
        m["the number of odd elements in the string i of the input."]=current_odd;
        all_odd.push_back(m["the number of odd elements in the string i of the input."]);
    }
    return all_odd;
}