    vector<string> roman_values={"m","cm","d","cd","c","xc","l","xl","x","ix","v","iv","i"};
    vector<int> values={1000,900,500,400,100,90,50,40,10,9,5,4,1};
    string result="";
    for (int i=0;i<values.size();i++)
    {
        while (number>=values[i])
        {
        result+=roman_values[i];
        number-=values[i];
        }
    }
    return result;
}


