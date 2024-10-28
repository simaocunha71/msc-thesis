    int n = arr.size();
    if(n==0) return true;
    int cnt = 0;
    for(int i=0;i<n-1;i++){
        if(arr[i]>arr[i+1]) cnt++;
    }
    if(arr[n-1]>arr[0]) cnt++;
    return cnt<=1;
}


A: Here is a Python solution for the above problems.

