    int n = arr.size();
    if(n == 0)
        return true;
    if(n == 1)
        return true;
    if(n == 2)
        if(arr[0] < arr[1])
            return true;
        else
            return false;
    int max_index = 0;
    for(int i = 0;i<n;i++)
    {
        if(arr[max_index] < arr[i])
            max_index = i;
    }
    if(max_index == n-1)
    {
        if(arr[max_index] < arr[0])
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    else if(max_index == 0)
    {
        for(int i = 1;i<n;i++)
        {
            if(arr[i] < arr[i-1])
            {
                return true;
            }
        }
        return false;
    }
    else
    {
        if(arr[max_index-1] < arr[max_index] && arr[max_index] < arr[max_index+1])
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

int main()
{
    vector<int> arr;
    arr.push_back(3);
    arr.push_back(4);
    arr.push_back(5);
    arr.push_back(1);
    arr.push_back(2);
    printf("%d",move_one_ball(arr));
    return 0;
}

*/






























































































