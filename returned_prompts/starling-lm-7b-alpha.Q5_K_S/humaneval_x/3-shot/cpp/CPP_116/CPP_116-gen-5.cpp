    vector<int> numbers;
    for (int i=0;i<arr.size();i++)
    {
        int number=arr[i];
        int number_bits=0;
        while (number!=0)
        {
            number_bits+=number%2;
            number/=2;
        }
        numbers.push_back(number_bits);
    }
    sort(numbers.begin(),numbers.end());
    vector<int> sorted_numbers;
    for (int i=0;i<arr.size();i++)
    {
        int number=arr[i];
        int number_bits=numbers[i];
        int power=0;
        int result=0;
        while (number_bits!=0)
        {
            result+=power*((number_bits%2)?1:0);
            number_bits/=2;
            power*=2;
        }
        sorted_numbers.push_back(result);
    }
    return sorted_numbers;
}


