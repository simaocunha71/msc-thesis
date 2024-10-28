int main()
{
    vector<int> numbers = {1, 2, 3, 2, 4};
    vector<int> result;

    for(int i = 0; i < numbers.size(); i++)
    {
        bool found = false;
        for(int j = 0; j < result.size(); j++)
        {
            if(numbers[i] == result[j])
            {
                found = true;
                break;
            }
        }
        if(!found)
        {
            result.push_back(numbers[i]);
        }
    }
    for(int i = 0; i < result.size(); i++)
    {
        printf("%d ", result[i]);
    }
    return 0;
}






















































































