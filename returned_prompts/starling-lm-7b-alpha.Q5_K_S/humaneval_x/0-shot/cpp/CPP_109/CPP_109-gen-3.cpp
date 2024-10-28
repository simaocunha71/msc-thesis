    if(arr.size()==0)
    {
        return true;
    }
    if(arr.size()==1)
    {
        return true;
    }
    if(arr.size()==2)
    {
        if(arr[0]>arr[1])
        {
            return false;
        }
        else
        {
            return true;
        }
    }
    if(arr.size()==3)
    {
        if(arr[0]>arr[1])
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    if(arr[0]<arr[arr.size()-1])
    {
        return true;
    }
    else
    {
        int pos=-1;
        for(int i=0;i<arr.size()-1;i++)
        {
            if(arr[i+1]>arr[i])
            {
                pos=i;
                break;
            }
        }
        if(pos==-1)
        {
            return false;
        }
        else
        {
            arr.erase(arr.begin()+pos);
            arr.push_back(arr[0]);
            arr.erase(arr.begin());
            goto A;
        }
    }
}
int main()
{
    vector<int> arr={3, 4, 5, 1, 2};
    printf("%d\n",move_one_ball(arr));
    return 0;
}




































































































































