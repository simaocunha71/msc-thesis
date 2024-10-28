    vector<int> vec;
    for (int i = 0; i < k; i++)
    {
        if (i == 0)
        {
            vec.push_back(arr[0]);
            continue;
        }
        for (int j = 0; j < vec.size(); j++)
        {
            if (arr[i] > vec[j])
            {
                vec.insert(vec.begin() + j, arr[i]);
                goto A;
            }
        }
        vec.push_back(arr[i]);
    }
    sort(vec.begin(), vec.end());
    return vec;
}

int main()
{
    vector<int> arr = {1,2,3,4,5,6,7,8,9,10};
    int k = 3;
    vector<int> vec = maximum(arr,k);
    for (int i = 0; i < vec.size(); i++)
    {
        printf("%d ", vec[i]);
    }
    return 0;
}
