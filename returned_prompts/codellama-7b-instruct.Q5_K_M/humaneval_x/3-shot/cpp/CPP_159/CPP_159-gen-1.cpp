    int total_eaten=number+remaining;
    if (total_eaten<need) return {total_eaten,0};
    else return {total_eaten-need, need};
}


