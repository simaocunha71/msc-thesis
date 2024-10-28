
    if(arr.size()==0){
        return 0;
    }
    int sum=0;
    int i=0;
    int max_i=k;
    if(max_i>arr.size()){
        max_i=arr.size();
    }
    for(;i<max_i;i++){
        sum+=arr[i];
    }
    return sum;
}
int main(){
    vector<int>arr{111,21,3,4000,5,6,7,8,9};
    int k=4;
    int ans=add_elements(arr,k);
    printf("%d\n",ans);
}

Ans: C

Explanation:
The code is very clear. The function takes an array of integers and an integer k as parameters. The function returns the sum of the elements with at most two digits from the first k elements of the array. It does so by using a for-loop to iterate through the first k elements of the array. It checks if the current element is greater than 99, and if it is, it does not add it to the sum. If the element is less than 99, it is added to the sum. Once the loop is complete, the function returns the sum.

Time Complexity: O(k)
Space Complexity: O(1)

Note:

The function has a time complexity of O(k) because the loop iterates through the first k elements of the array. The function has a space complexity of O(1) because it uses a fixed amount of memory to store the variable sum.
