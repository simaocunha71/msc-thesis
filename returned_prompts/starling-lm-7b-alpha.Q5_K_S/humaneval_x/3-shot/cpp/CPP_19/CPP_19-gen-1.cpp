    map<string,int> m;
    m["zero"]=0;
    m["one"]=1;
    m["two"]=2;
    m["three"]=3;
    m["four"]=4;
    m["five"]=5;
    m["six"]=6;
    m["seven"]=7;
    m["eight"]=8;
    m["nine"]=9;

    vector<string> all_nums;
    char chr;
    for (int i=0;i<numbers.length();i++)
    {
        chr=numbers[i];
        if (chr==' ')
        continue;
        all_nums.push_back(string(1,chr));
    }
    sort(all_nums.begin(),all_nums.end());
    string s;
    for (int i=0;i<all_nums.size();i++)
    {
        s+=m[all_nums[i]];
        if (i!=all_nums.size()-1)
        s+=" ";
    }
    return s;
}


