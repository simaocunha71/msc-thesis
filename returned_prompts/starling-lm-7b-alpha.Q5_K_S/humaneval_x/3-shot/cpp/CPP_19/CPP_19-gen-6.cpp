    map<string, int> m;
    int i,j;
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

    string str;
    vector<string> all_numbers;
    for (i=0;i<numbers.length();i++)
    {
        if (numbers[i]==' '){
            continue;
        }
        str="";
        for (j=i;j<i+2;j++)
        {
            str+=numbers[j];
        }
        all_numbers.push_back(str);
    }
    sort(all_numbers.begin(), all_numbers.end());
    string result="";
    for (i=0;i<all_numbers.size();i++)
    {
        result+=m[all_numbers[i]]+(i==all_numbers.size()-1?"": " ");
    }
    return result;
}


