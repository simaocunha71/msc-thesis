    vector<int> result;
    result.clear();
    int length = numbers.size();
    for(int i = 0; i < length; i++)
    {
        bool is_exist = false;
        for(int j = 0; j < result.size(); j++)
        {
            if(numbers[i] == result[j])
            {
                is_exist = true;
                break;
            }
        }
        if(!is_exist)
            result.push_back(numbers[i]);
    }
    return result;
}

/*
From a vector of integers, remove all elements that occur more than once.
Keep order of elements left the same as in the input.
>>> remove_duplicates({1, 2, 3, 2, 4})
{1, 3, 4}
*/

vector<int> remove_duplicates2(vector<int> numbers)
{
    vector<int> result;
    result.clear();
    if(numbers.size() == 0)
        return result;
    result.push_back(numbers[0]);
    int length = numbers.size();
    for(int i = 1; i < length; i++)
    {
        if(numbers[i] != result.back())
            result.push_back(numbers[i]);
    }
    return result;
}

int main(void)
{
    vector<int> numbers;
    numbers.push_back(1);
    numbers.push_back(2);
    numbers.push_back(3);
    numbers.push_back(2);
    numbers.push_back(4);
    numbers.push_back(5);
    numbers.push_back(6);
    numbers.push_back(3);
    numbers.push_back(7);
    numbers.push_back(8);

    vector<int> result1 = remove_duplicates(numbers);
    vector<int> result2 = remove_duplicates2(numbers);

    printf("result1:");
    for(int i = 0; i