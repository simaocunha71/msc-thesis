    vector<pair<int,string>> roman_values={{1000,"m"},{900,"cm"},{500,"d"},{400,"cd"},{100,"c"},{90,"xc"},{50,"l"},{40,"xl"},{10,"x"},{9,"ix"},{5,"v"},{4,"iv"},{1,"i"}};
    string result="";
    int i,current_value;
    for (i=0;i<roman_values.size();i++)
    {
        current_value=number/roman_values[i].first;
        result+=string(current_value,roman_values[i].second);
        number-=current_value*roman_values[i].first;
        if (number==0)
        return result;
    }
    return result;
}


