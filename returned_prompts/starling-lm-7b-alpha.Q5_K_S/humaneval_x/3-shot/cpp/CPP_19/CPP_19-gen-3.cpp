    map<string,int> number_map;
    number_map["zero"]=0;
    number_map["one"]=1;
    number_map["two"]=2;
    number_map["three"]=3;
    number_map["four"]=4;
    number_map["five"]=5;
    number_map["six"]=6;
    number_map["seven"]=7;
    number_map["eight"]=8;
    number_map["nine"]=9;
    string number;
    int i,j;
    int number_size=numbers.size();
    vector<int> number_list;
    for (i=0;i<number_size;i++)
    {
        while (numbers[i]!=' ')
        {
            number+=numbers[i];
            i+=1;
        }
        number_list.push_back(number_map[number]);
        number="";
    }
    sort(number_list.begin(),number_list.end());
    string result="";
    for (i=0;i<number_size;i++)
    {
        if (i!=0)
            result+=' ';
        if (number_list[i]==0)
            result+="zero";
        if (number_list[i]==1)
            result+="one";
        if (number_list[i]==2)
            result+="two";
        if (number_list[i]==3)
            result+="three";
        if (number_list[i]==4)
            result+="four";
        if (number_list[i]==5)
            result+="five";
        if (number_list[i]==6)
            result+="six";
        if (number_list[i]==7)
            result+="seven";
        if (number_list[i]==8)
            result+="eight";
        if (number_list[i]==9)
            result+="nine";
    }
    return result;
}












