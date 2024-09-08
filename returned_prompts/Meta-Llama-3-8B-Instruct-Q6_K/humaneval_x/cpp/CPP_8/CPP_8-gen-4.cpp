    if(numbers.empty())
    {
        return {0, 1};
    }
    int sum = 0;
    int product = 1;
    for(int i = 0; i < numbers.size(); i++)
    {
        sum += numbers[i];
        product *= numbers[i];
    }
    return {sum, product};
}

int main()
{
    vector<int> numbers = {1, 2, 3, 4};
    vector<int> result = sum_product(numbers);
    printf("Sum and product of vector elements are: %d %d\n", result[0], result[1]);
    return 0;
}

