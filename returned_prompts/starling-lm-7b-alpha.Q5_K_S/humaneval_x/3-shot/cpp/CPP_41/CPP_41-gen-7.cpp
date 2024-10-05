    int i;
    int collisions=0;
    int left_speed=n;
    int right_speed=n;
    for (i=0;i<n;i++)
    {
        if (left_speed<right_speed)
        {
            collisions+=right_speed-left_speed;
            left_speed+=n;
        }
        else
        {
            collisions+=left_speed-right_speed;
            right_speed+=n;
        }
    }
    return collisions;
}



