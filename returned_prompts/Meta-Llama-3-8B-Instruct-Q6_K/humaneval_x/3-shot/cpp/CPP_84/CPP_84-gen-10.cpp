    int sum = 0, binary = N;
    while(binary > 0)
    {
        sum += binary % 2;
        binary /= 2;
    }
    string res = "";
    while(sum > 0)
    {
        res = (sum % 2 == 1) ? "1" + res : "0" + res;
        sum /= 2;
    }
    return res;
}
```



Here are the solutions:

