/*
The solution should start by checking if the two intervals intersect at all. If they don't, return "NO".
If the intervals intersect, find the intersection interval by taking the maximum of start of the first interval and the second one, and the minimum of the end of the first interval and the second one.
Once you have the intersection interval, find its length by subtracting its start from its end.
Finally, check if this length is a prime number. If it is, return "YES", otherwise return "NO".
*/

B:
    int start = max(interval1[0],interval2[0]);
    int end = min(interval1[1],interval2[1]);
    if(start > end)
        return "NO";
    int len = end - start;
    if(len < 2)
        return "NO";
    for(int i = 2; i*i <= len; i++){
        if(len % i == 0)
            return "NO";
    }
    return "YES";
}


int main(){
    vector<int> interval1{1,2};
    vector<int> interval2{2,3};
    printf("%s\n",intersection(interval1,interval2).c_str());
    vector<int> interval3{-1,1};
    vector<int> interval4{0,4};
    printf("%s\n",intersection(interval3,interval4).c_str());
    vector<int> interval5{-3,-1};
    vector<int> interval6{1,5};
    printf("%s\n",intersection(interval5,interval6).c_str());
    return 0;
}

























































































































