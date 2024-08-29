    // sort the array
    sort(arr.begin(),arr.end());

    // return the first k elements
    return vector<int>(arr.begin(),arr.begin()+k);
}

vector<int> maximum(vector<int> arr,int k){
    // create a vector with the size k
    vector<int> max_k;

    // loop over the array
    for(int i=0;i<k;i++){
        // find the maximum element
        int max=arr[0];
        int max_index=0;
        for(int j=0;j<arr.size();j++){
            if(arr[j]>max){
                max=arr[j];
                max_index=j;
            }
        }

        // add the maximum element to the vector
        max_k.push_back(max);

        // remove the maximum element from the array
        arr.erase(arr.begin()+max_index);
    }

    // sort the vector
    sort(max_k.begin(),max_k.end());

    // return the vector
    return max_k;
}

vector<int> maximum(vector<int> arr,int k){
    // create a vector with the size k
    vector<int> max_k;

    // loop over the array
    for(int i=0;i<k;i++){
        // find the maximum element
        int max=arr[0];
        int max_index=0;
        for(int j=0;j<arr.size();j++){
            if(arr[j]>max){
                max=arr[j];
                max_index=j;
            }
        }

        // add the maximum element to the vector
        max_k.push_back(max);

        // remove the maximum element from the array
        arr.erase(arr.begin()+max_index);
    }

    // sort the vector
    sort(max_k.begin(),max_k.end());

    // return the vector
    return max_k;
}

vector<int> maximum(vector<int> arr,int k){
    // create a vector with the size k
    vector<int> max_k;

    // loop over the array
    for(int i=0;i<k;i++){
        // find the maximum element
        int max=arr[0];
        int max_index=0;
        for(int j=0;j<arr.size();j++){
            if(arr[j]>max){
                max=arr[j];
                max_index=j;
            }
        }

        // add the maximum element to the vector
        max_k.push_back(max);

        // remove the maximum element from the array
        arr.erase(arr.begin()+max_index);
    }

