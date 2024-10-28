    int sum = 0;
    for (int i = 0; i < array.size(); i++)
    {
        sum += array[i];
    }
    if (sum % 2 == 0)
    {
        sort(array.begin(), array.end(), greater<int>());
    }
    else
    {
        sort(array.begin(), array.end());
    }
    return array;
}

int main()
{
    vector<int> array{ 2, 4, 3, 0, 1, 5 };
    vector<int> array1{ 2, 4, 3, 0, 1, 5, 6 };
    vector<int> array2{ 3, 4, 5, 1, 2 };
    vector<int> array3{ 1, 2, 3, 4, 5 };
    vector<int> array4{ 5, 4, 3, 2, 1 };
    vector<int> array5{ 5, 4, 3, 2, 1, 0 };
    vector<int> array6{ 5, 4, 3, 2, 1, 0, 6 };
    vector<int> array7{ 0, 1, 2, 3, 4, 5 };
    vector<int> array8{ 0, 1, 2, 3, 4, 5, 6 };
    vector<int> array9{ 6, 5, 4, 3, 2, 1, 0 };
    vector<int> array10{ 6, 5, 4, 3, 2, 1, 0, 7 };
    printf("array: %s\n", sort_array(array).data());
    printf("array1: %s\n", sort_array(array1).data());
    printf("array2: %s\n", sort_array(array2).data());
    printf("array3: %s\n", sort_array(array3).data());
    printf("array4: %s\n", sort_array