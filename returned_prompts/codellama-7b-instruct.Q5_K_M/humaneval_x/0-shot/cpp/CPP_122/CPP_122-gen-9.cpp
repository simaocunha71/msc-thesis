    int sum = 0;
    for(int i = 0;i<k;i++){
        if(arr[i] >= 100){
            goto A;
        }
        sum += arr[i];
    }
    return sum;
}
int main(){
    vector<int> arr = {111,21,3,4000,5,6,7,8,9};
    int k = 4;
    printf("sum = %d\n",add_elements(arr,k));
    return 0;
}



Ans: C 
Explanation:

The time complexity of the above solution is O(k) and space complexity is O(1).

The solution is correct because the if statement checks if any of the elements
in the first k elements of the array is greater than 100. If such an element
is found, then the goto statement is executed and the function returns 0.
This ensures that the solution is correct.