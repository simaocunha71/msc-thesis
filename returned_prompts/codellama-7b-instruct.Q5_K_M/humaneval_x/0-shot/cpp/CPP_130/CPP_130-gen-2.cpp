/*
The first thing I thought of was a recursive solution. I decided to make the 
function tri(n) to return a vector of the first n+1 numbers of the Tribonacci 
sequence. The first number of the sequence is 1, the next number is 2, and so on. 
The base case is tri(0) = {1}, because the first number of the sequence is always 1.
*/
vector<int> tri(int n){
    if(n == 0) return vector<int>{1};
    else{
        vector<int> v = tri(n-1);
        v.push_back(v[n-1] + v[n-2] + v[n-3]);
        return v;
    }
}

