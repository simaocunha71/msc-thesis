    vector<int> odd_vec;
    int i = n;
    while(i>1){
        if(i%2==0)
            i/=2;
        else{
            i = 3*i+1;
            odd_vec.push_back(i);
        }
    }
    sort(odd_vec.begin(), odd_vec.end());
    return odd_vec;
}

/*
B:
vector<int> get_odd_collatz(int n){
    vector<int> odd_vec;
    while(n>1){
        odd_vec.push_back(n);
        n = n%2 == 0 ? n/2 : 3*n+1;
    }
    sort(odd_vec.begin(), odd_vec.end());
    return odd_vec;
}
*/
