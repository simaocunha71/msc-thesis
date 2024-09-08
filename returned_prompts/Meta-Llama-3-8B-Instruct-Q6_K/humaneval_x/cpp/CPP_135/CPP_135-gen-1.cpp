    int i;
    for(i=1; i<arr.size(); i++){
        if(arr[i] <= arr[i-1]) return i-1;
    }
    return -1;
}

int main(){
    vector<int> arr1 = {1,2,4,3,5};
    vector<int> arr2 = {1,2,3};
    cout << "Largest index of an element which is not greater than or equal to the element immediately preceding it: " << can_arrange(arr1) << endl;
    cout << "Largest index of an element which is not greater than or equal to the element immediately preceding it: " << can_arrange(arr2) << endl;
    return 0;
}

