    if (n>m)
        return "-1";
    else
    {
        float avg=(float(n)+float(m))/2;
        int avg_int=int(avg);
        float decimal_part=avg-avg_int;
        if (decimal_part>=0.5)
            avg_int+=1;
        return to_string(avg_int);
    }
}

