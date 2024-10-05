    vector<int> even_numbers;
    if  (a>b)
    {
    int temp=a;
    a=b;
    b=temp;
    }
    for  (int i=a;i<=b;i++)
    if  (i%2==0)
    even_numbers.push_back(i);
    return even_numbers;
}


