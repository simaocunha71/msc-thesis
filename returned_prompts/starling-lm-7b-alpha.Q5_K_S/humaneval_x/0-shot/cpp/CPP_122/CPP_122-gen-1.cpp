    int sum=0;
    for(int i=0;i<k;i++){
        sum+=arr[i];
    }
    return sum;
}

/*
Given a non-empty vector of integers arr and an integer k, return
the sum of the elements with at most two digits from the first k elements of arr.

Example:

    Input: arr = {111,21,3,4000,5,6,7,8,9}, k = 4
    Output: 24 # sum of 21 + 3

Constraints:
    1. 1 <= len(arr) <= 100
    2. 1 <= k <= len(arr)
*/
int main()
{
    vector<int> arr;
    int k;
    scanf("%d",&k);
    for(int i=0;i<k;i++){
        int temp;
        scanf("%d",&temp);
        arr.push_back(temp);
    }
    printf("%d\n",add_elements(arr,k));
    return 0;
}

*/

















































































































































































































































