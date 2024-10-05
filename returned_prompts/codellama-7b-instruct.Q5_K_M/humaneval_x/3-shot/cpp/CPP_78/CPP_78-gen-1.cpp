    int i;
    int count=0;
    string num_hex[16] = {"0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"};
    for (i=0;i<16;i++)
    if (num.find(num_hex[i])!=string::npos)
    if (is_prime(i))
    count+=1;
    return count;
}
int count_pr