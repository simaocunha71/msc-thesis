    float sum=0.0, mean, mad = 0.0;
    int i;

    for(i = 0; i < numbers.size(); i++)
    {
       sum += numbers[i];
    }

    mean = sum/numbers.size();

    for(i = 0; i < numbers.size(); i++)
    {
       mad += abs(numbers[i] - mean);
    }

    return mad/numbers.size();
}

