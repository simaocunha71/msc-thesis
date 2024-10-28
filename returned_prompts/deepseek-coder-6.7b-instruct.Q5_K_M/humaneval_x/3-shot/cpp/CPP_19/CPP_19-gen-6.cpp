    map<string,int> number_dict;
    number_dict["zero"]=0;
    number_dict["one"]=1;
    number_dict["two"]=2;
    number_dict["three"]=3;
    number_dict["four"]=4;
    number_dict["five"]=5;
    number_dict["six"]=6;
    number_dict["seven"]=7;
    number_dict["eight"]=8;
    number_dict["nine"]=9;

    vector<string> number_list;
    string temp;
    for  (int i=0;i<numbers.length();i++)
    {
        if  (numbers[i]==' ')
        {
            number_list.push_back(temp);
            temp="";
        }
        else
        {
            temp+=numbers[i];
        }
    }
    number_list.push_back(temp);
    sort(number_list.begin(), number_list.end(), [&number_dict](const string &a, const string &b)
    {
        return number_dict[a] < number_dict[b];
    });
    temp="";
    for  (int i=0;i<number_list.size();i++)
    {
        temp+=number_list[i];
        if  (i<number_list.size()-1)
        temp+=' ';
    }
    return temp;
}



