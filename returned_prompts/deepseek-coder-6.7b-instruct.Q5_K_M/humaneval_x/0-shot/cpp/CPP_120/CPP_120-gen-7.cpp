    //sort the array in decreasing order
    sort(arr.begin(),arr.end(),greater<int>());
    //initialize the result vector
    vector<int> res;
    //push the first k elements into the result vector
    for(int i=0;i<k;i++)
        res.push_back(arr[i]);
    //return the result vector
    return res;
}

int main() {
    vector<int> arr = {4, -4, 4};
    int k = 2;
    vector<int> res = maximum(arr,k);
    for(int i=0; i<res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}

*/


