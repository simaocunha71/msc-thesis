    if(q.size()!=0 && q!=vector<int>(q.rbegin(),q.rend())){
        return false;
    }
    int sum=0;
    for(int i=0;i<q.size();i++){
        sum+=q[i];
    }
    return sum<=w;
} // This function will return true if the vector q will fly, and false otherwise. It checks if the vector is balanced (palindromic) and if the sum of its elements is less than or equal to the maximum possible weight w.