    vector<int> res;
    vector<int> l1_copy(l1);
    sort(l1_copy.begin(), l1_copy.end());
    vector<int> l2_copy(l2);
    sort(l2_copy.begin(), l2_copy.end());
    int i=0, j=0;
    while(i<l1_copy.size() && j<l2_copy.size()){
        if(l1_copy[i] == l2_copy[j]){
            res.push_back(l1_copy[i]);
            i++;
            j++;
        }
        else if(l1_copy[i] < l2_copy[j]){
            i++;
        }
        else{
            j++;
        }
    }
    return res;
}

int main() {
    vector<int> l1={1, 4, 3, 34, 653, 2, 5};
    vector<int> l2={5, 7, 1, 5, 9, 653, 121};
    vector<int> res = common(l1, l2);
    for(int i=0; i<res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}
// Output: 1 5 653
