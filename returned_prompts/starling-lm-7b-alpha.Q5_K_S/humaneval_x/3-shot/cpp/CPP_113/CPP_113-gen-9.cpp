    vector<string> result;
    int i;
    map<int,string> m;
    m[0]= "the number of odd elements ";
    m[1]= "n the str";
    m[2]= "ng ";
    m[3]= " of the ";
    m[4]= "nput.";
    for (i=0;i<lst.size();i++)
    {
        int odd_count=0;
        int j;
        for (j=0;j<lst[i].length();j++)
        {
            if (int(lst[i][j])%2==1)
            {
                odd_count+=1;
            }
        }
        string res;
        for (auto elt: m)
        {
            res+=elt.second;
        }
        res.replace(res.find("n"), 1, to_string(odd_count));
        res.replace(res.find("str"), 1, lst[i]);
        result.push_back(res);
    }
    return result;
}



