    if(arr.size() == 0)
        return true;
    int max = 0;
    for(int i = 0; i < arr.size(); i++)
    {
        if(arr[i] > max)
            max = arr[i];
    }
    int index = arr.size() - 1;
    while(index >= 0)
    {
        if(arr[index] != max)
        {
            index--;
        }
        else
        {
            if(index == 0)
                return true;
            else
            {
                arr.erase(arr.begin() + index);
                arr.insert(arr.begin(), arr[index]);
                index = arr.size() - 2;
                max = 0;
                for(int i = 0; i < arr.size(); i++)
                {
                    if(arr[i] > max)
                        max = arr[i];
                }
            }
        }
    }
    return false;
}
int main()
{
    vector<int> arr = {3, 4, 5, 1, 2};
    printf("%d\n", move_one_ball(arr));
    return 0;
}

*/









































































































































































































