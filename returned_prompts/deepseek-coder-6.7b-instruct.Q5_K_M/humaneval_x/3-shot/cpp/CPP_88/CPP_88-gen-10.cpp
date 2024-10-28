    vector<int> sortedArray(array);
    int sum = array.front() + array.back();

    if(sum % 2 == 0){
        sort(sortedArray.begin(), sortedArray.end(), greater<int>());
    }
    else{
        sort(sortedArray.begin(), sortedArray.end());
    }

    return sortedArray;
}


