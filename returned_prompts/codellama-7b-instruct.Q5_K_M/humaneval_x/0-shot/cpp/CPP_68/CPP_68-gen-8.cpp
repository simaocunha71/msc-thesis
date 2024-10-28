    vector<int> result;
    int smallest = INT_MAX;
    int smallest_index = -1;
    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i] % 2 == 0 && arr[i] < smallest)
        {
            smallest = arr[i];
            smallest_index = i;
        }
    }
    if (smallest_index != -1)
    {
        result.push_back(smallest);
        result.push_back(smallest_index);
        arr.erase(arr.begin() + smallest_index);
        goto A;
    }
    if (result.size() == 0)
        result.push_back(0);
    return result;
}
int main()
{
    vector<int> arr = { 5, 0, 3, 0, 4, 2 };
    vector<int> result = pluck(arr);
    for (int i = 0; i < result.size(); i++)
    {
        printf("%d ", result[i]);
    }
    return 0;
}
