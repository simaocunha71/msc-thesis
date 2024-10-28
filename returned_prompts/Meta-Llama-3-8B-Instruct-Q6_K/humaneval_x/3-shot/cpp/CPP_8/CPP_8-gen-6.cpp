    int sum=0;
    int product=1;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        product*=numbers[i];
    }
    return {sum,product};
} // end of function sum_product
// test the function
int main()
{
    vector<int> numbers;
    cout << sum_product(numbers).at(0) << endl; // prints 0
    cout << sum_product(numbers).at(1) << endl; // prints 1
    numbers.push_back(1);
    numbers.push_back(2);
    numbers.push_back(3);
    numbers.push_back(4);
    cout << sum_product(numbers).at(0) << endl; // prints 10
    cout << sum_product(numbers).at(1) << endl; // prints 24
    return 0;
} // end of main
// end of program
// end of file
// end of end

