    int total_eaten = number+need;
    int remaining_eaten = remaining-(need-number);
    if (remaining_eaten<0)
    remaining_eaten=0;
    return vector<int>{total_eaten,remaining_eaten};
}



