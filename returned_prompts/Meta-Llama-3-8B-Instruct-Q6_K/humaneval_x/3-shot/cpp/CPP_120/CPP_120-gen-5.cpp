    priority_queue<int> pq;
    for(int i=0; i<arr.size(); i++){
        pq.push(arr[i]);
    }
    vector<int> res(k);
    for(int i=0; i<k; i++){
        res[i] = pq.top();
        pq.pop();
    }
    return res; 
}
