    if(arr.size() == 0)
        return true;
    if(arr.size() == 1)
        return true;

    for(int i = 0; i < arr.size() - 1; i++)
    {
        if(arr[i] > arr[i+1])
        {
            return false;
        }
    }

    return true;
}

int main()
{
    vector<int> a = {3,4,5,1,2};
    if(move_one_ball(a))
        printf("True\n");
    else
        printf("False\n");
    return 0;
}

