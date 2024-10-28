    int i;
    int result=0;
    for (i=0;i<n;i++)
    {
        int left_car=i;
        int right_car=n-i-1;
        if (left_car>right_car)
        {
            result+=right_car-left_car;
        }
        else if (right_car>left_car)
        {
            result+=left_car-right_car;
        }
    }
    return result;
}



