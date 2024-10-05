    int sum = 0;
    int count = 0;
    for (int i=2; i<n; i+=2){
        sum += i;
        count++;
        if (sum == n)
            return true;
    }
    return false;
}

