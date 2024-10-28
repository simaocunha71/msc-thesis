    int i,j;
    for (i=0;i<num.size();i++)
    {
        if (num[i]>='0'&&num[i]<='9')
        {
            j=num[i]-'0';
            if (j==2||j==3||j==5||j==7)
            return 1;
        }
        if (num[i]>='A'&&num[i]<='F')
        {
            j=num[i]-'A';
            if (j==11||j==13)
            return 1;
        }
    }
    return 0;
}

int main()
{
    /*
    vector<float> numbers;
    numbers.push_back(1.0);
    numbers.push_back(2.0);
    numbers.push_back(3.0);
    numbers.push_back(4.0);
    numbers.push_back(5.0);
    float t=5.0;
    float r=3.0;
    printf("%d\n",numbers.size());
    printf("%d\n",(int)t);
    printf("%d\n",(int)r);
    */
    vector<float> numbers;
    numbers.push_back(1.0);
    numbers.push_back(2.8);
    numbers.push_back(3.0);
    numbers.push_back(4.0);
    numbers.push_back(5.0);
    numbers.push_back(2.0);
    printf("%d\n",has_close_elements(numbers,0.3));
    string paren_string="( ) (( )) (( )( ))";
    vector<string> all_parens=separate_paren_groups(paren_string);
    for (int i=0;i<all_parens.size();i++)
    printf("\"%s\"\n",all_parens[i].c_str());
    float number=3.5;
    float decimal=truncate_number(number);
    printf("%f\n",decimal);
