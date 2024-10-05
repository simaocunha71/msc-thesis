    vector<int> even_numbers;
    int i;
    if  (a<b)
    for  (i=a;i<=b;i++)
    if  (i%2==0)
    even_numbers.push_back(i);
    else
    for  (i=b;i<=a;i++)
    if  (i%2==0)
    even_numbers.push_back(i);
    return even_numbers;
}


