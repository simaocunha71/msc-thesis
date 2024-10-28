    for (int i=1;i<numbers.size();i++)
    {
        numbers.insert(numbers.begin()+i,delimeter);
        i++;
    }
    return numbers;
}


