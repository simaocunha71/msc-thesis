    int n=arr.size();
    int changes=0;
    int left=n-1;
    int right=0;
    while(left>=right){
        if(arr[left]==arr[right]){
            left--;
            right++;
        }
        else{
            changes++;
            int max_val=INT_MIN;
            for(int i=0;i<n;i++){
                max_val=max(max_val,arr[i]);
            }
            arr[left]=max_val;
            changes++;
            left--;
            right++;
        }
    }
    return changes;
}

int main()
{
    vector<int> arr={1,2,3,5,4,7,9,6};
    cout<<smallest_change(arr);
    return 0;
}

