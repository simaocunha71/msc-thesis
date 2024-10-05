    sort(l1.begin(), l1.end());
    sort(l2.begin(), l2.end());
    vector<int> result;

B:
    int i = 0, j = 0;
    while(i < l1.size() && j < l2.size()){
        if(l1[i] < l2[j])
            i++;
        else if(l2[j] < l1[i])
            j++;
        else{
            result.push_back(l2[j]);
            i++;
            j++;
        }
    }
    return result;
}
int main(){
    vector<int> l1 = {1, 4, 3, 34, 653, 2, 5};
    vector<int> l2 = {5, 7, 1, 5, 9, 653, 121};
    vector<int> res = common(l1, l2);
    for(int i = 0; i< res.size(); i++)
        printf("%d ", res[i]);
    return 0;
}


A: 

//This solution is correct but it is not efficient. The time complexity of this solution is O(n log n) due to sorting.
//We can solve this problem in linear time by using a unordered map.


