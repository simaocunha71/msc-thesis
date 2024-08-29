    //O(n) time complexity
    //O(n) space complexity
    //sort the vector in descending order
    sort(arr.begin(),arr.end(),greater<int>());
    //erase the elements from the kth position to the end of the vector
    arr.erase(arr.begin()+k,arr.end());
    return arr;

B:
    //O(nlogk) time complexity
    //O(k) space complexity
    //create a min heap of size k
    priority_queue<int,vector<int>,greater<int>> pq;
    //push the first k elements into the min heap
    for(int i=0;i<k;i++){
        pq.push(arr[i]);
    }
    //push the remaining elements into the min heap
    //if the element is greater than the top of the min heap, pop the top element and push the new element
    for(int i=k;i<arr.size();i++){
        if(arr[i]>pq.top()){
            pq.pop();
            pq.push(arr[i]);
        }
    }
    //create a vector to store the elements of the min heap
    vector<int> res;
    //pop the elements from the min heap and store them in the vector
    while(!pq.empty()){
        res.push_back(pq.top());
        pq.pop();
    }
    //reverse the vector to get the elements in descending order
    reverse(res.begin(),res.end());
    return res;

C:
    //O(nlogk) time complexity
    //O(k) space complexity
    //create a max heap of size k
    priority_queue<int> pq;
    //push the first k elements into the max heap
    for(int i=0;i<k;i++){
        pq.push(arr[i]);
    }
    //push the remaining elements into the max heap
    //if the element is smaller than the top of the max heap, pop the top element and push the new element
    for(int i=k;i<arr.size();i++){
        if(arr[i]<pq.top()){
            pq.pop();
            pq.push(arr[i]);
        }
    }
    //create a vector to store the elements of the max heap
    vector<int> res;
    //pop the elements from the max heap and store them in the vector
    while(!pq.empty()){
        res.push_back(pq.top());
        pq.pop();
    }
    //reverse the vector to get the elements in descending order
    reverse(res.begin(),res.end());
    return res;

D:
    //