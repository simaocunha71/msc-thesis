    float diff, min_diff, smallest, largest;
    int smallest_index, largest_index;
    int i;
    smallest_index=0;
    smallest=numbers[0];
    largest_index=0;
    largest=numbers[0];
    min_diff=10000000000;
    for (i=1;i<numbers.size();i++)
    {
        diff=numbers[i]-numbers[i-1];
        if (diff<min_diff)
        {
            smallest=numbers[i-1];
            smallest_index=i-1;
            largest=numbers[i];
            largest_index=i;
            min_diff=diff;
        }
        if (diff==min_diff)
        {
            smallest=numbers[smallest_index];
            largest=numbers[largest_index];
        }
    }
    return {smallest, largest};
}



