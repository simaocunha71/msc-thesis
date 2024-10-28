    int size = (int)lst.size();
    if(size == 0)
        return 0;
    float sum = 0;
    for(int i = 0; i < size; i++){
        float number = lst[i];
        if(number < 0 || number != (int)number)
            continue;
        sum += pow(number, 2);
    }
    return sum;
}

