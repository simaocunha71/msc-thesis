    int sum=0;
    for (int i=0; i<lst.size(); i++)
    {
        if (i%3==0) sum+=lst[i]*lst[i];
        else if (i%4==0 && i%3!=0) sum+=pow(lst[i],3);
    }
    return sum;
}
// or
int sum_squares(vector<int> lst){
    int sum=0;
    for (int i=0; i<lst.size(); i++)
    {
        if (i%3==0) sum+=lst[i]*lst[i];
        else if (i%4==0 && i%3!=0) sum+=pow(lst[i],3);
    }
    return sum;
}
// or
int sum_squares(vector<int> lst){
    int sum=0;
    for (int i=0; i<lst.size(); i++)
    {
        if (i%3==0) sum+=pow(lst[i],2);
        else if (i%4==0 && i%3!=0) sum+=pow(lst[i],3);
    }
    return sum;
}

// or
int sum_squares(vector<int> lst){
    int sum=0;
    for (int i=0; i<lst.size(); i++)
    {
        if (i%3==0) sum+=lst[i]*lst[i];
        else if (i%4==0 && i%3!=0) sum+=pow(lst[i],3);
    }
    return sum;
}  // or 1-3 for all i in lst
// or
int sum_squares(vector<int> lst){
    int sum=0;
    for (int i=0; i<lst.size(); i++)
    {
        if (i%3==0) sum+=lst[i]*lst[i];
        else if (i%4==0 && i%3!=0) sum+=pow(lst[i],3);
    }
    return sum;
}  // or 1-3 for all i in lst
// or
int sum_squares(vector<int> lst){
    int sum=0;
    for (int i=0; i<lst.size(); i++)
    {
        if (i%3==0) sum+=lst[i]*lst[i];
        else if (i%4==0 && i%3!=0) sum+=pow(lst[i],3);
    }
    return sum;
}