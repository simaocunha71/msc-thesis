    int i;
    int num_of_collisions=0;
    int num_of_left_cars=n;
    int num_of_right_cars=n;
    for (i=0;i<n;i++){
        if (num_of_left_cars<num_of_right_cars)
        {
            num_of_left_cars++;
            num_of_right_cars--;
        }
        else if (num_of_left_cars>num_of_right_cars)
        {
            num_of_left_cars--;
            num_of_right_cars++;
        }
        else
        {
            num_of_collisions++;
            num_of_left_cars--;
            num_of_right_cars--;
        }
    }
    return num_of_collisions;
}



