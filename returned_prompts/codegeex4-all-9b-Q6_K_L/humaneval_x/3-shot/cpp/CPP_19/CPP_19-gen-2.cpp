    map<string,int> numberals;
    numberals["zero"]=0;
    numberals["one"]=1;
    numberals["two"]=2;
    numberals["three"]=3;
    numberals["four"]=4;
    numberals["five"]=5;
    numberals["six"]=6;
    numberals["seven"]=7;
    numberals["eight"]=8;
    numberals["nine"]=9;
    vector<int> numbers_as_ints;
    string current_number;
    int i;
    for (i=0;i<numbers.length();i++)
    {
        if (numbers[i]!=' ')
        {
        current_number+=numbers[i];
        }
        else{
            numbers_as_ints.push_back(numberals[current_number]);
            current_number="";
        }
    }
    numbers_as_ints.push_back(numberals[current_number]);

    int j,k;
    for (j=0;j<numbers_as_ints.size();j++)
    for (k=j+1;k<numbers_as_ints.size();k++)
    {
        if (numbers_as_ints[j]>numbers_as_ints[k])
        {
            int temp=numbers_as_ints[j];
            numbers_as_ints[j]=numbers_as_ints[k];
            numbers_as_ints[k]=temp;
        }
    }
    current_number="";
    for (i=0;i<numbers_as_ints.size();i++){
        if (numbers_as_ints[i]==0) current_number+="zero ";
        if (numbers_as_ints[i]==1) current_number+="one ";
        if (numbers_as_ints[i]==2) current_number+="two ";
        if (numbers_as_ints[i]==3) current_number+="three ";
        if (numbers_as_ints[i]==4) current_number+="four ";
        if (numbers_as_ints[i]==5) current_number+="five ";
        if (numbers_as_ints[i]==6) current_number+="six ";
        if (numbers_as_ints[i]==7) current_number+="seven ";
        if (numbers_as_ints[i]==8) current_number+="eight ";
        if (numbers_as_ints[i]==9) current_number+="nine ";
    }

    current_number.pop_back();
    return current_number;
}

