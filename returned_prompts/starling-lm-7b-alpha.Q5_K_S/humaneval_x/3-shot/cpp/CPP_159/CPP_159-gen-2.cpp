    int total_eaten=number+need;
    int remaining_after_meal=remaining-need;
    if (remaining_after_meal<0)
    {
        total_eaten+=remaining_after_meal;
        remaining_after_meal=0;
    }
    return vector<int>{total_eaten,remaining_after_meal};
}




