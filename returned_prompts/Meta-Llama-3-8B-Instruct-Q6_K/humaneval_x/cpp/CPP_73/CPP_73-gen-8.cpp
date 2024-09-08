    int n = arr.size();
    int count = 0;
    vector<int> left, right;
    for(int i = 0; i < n; i++){
        if(arr[i] != arr[n-i-1])
            count++;
    }
    return count;
}
int main()
{
    vector<int> arr={1,2,3,5,4,7,9,6};
    printf("smallest change: %d",smallest_change(arr));
    return 0;
}
