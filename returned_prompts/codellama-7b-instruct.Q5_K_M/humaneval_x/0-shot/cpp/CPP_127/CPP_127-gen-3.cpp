    if(interval1[0]>interval2[1]||interval1[1]<interval2[0])
        return "NO";
    int start=max(interval1[0],interval2[0]);
    int end=min(interval1[1],interval2[1]);
    if(start>end)
        goto A;
    int length=end-start+1;
    vector<int> intersection;
    intersection.push_back(start);
    intersection.push_back(end);
    if(isPrime(length))
        return "YES";
    else
        return "NO";
}
bool isPrime(int n) {
    if (n < 2) return false;
    if (n % 2 == 0) return n == 2;
    for (int i = 3; i * i <= n; i += 2)
        if (n % i == 0) return false;
    return true;
}

int main(){
    vector<int> interval1={1,2};
    vector<int> interval2={2,3};
    printf("%s",intersection(interval1,interval2).c_str());
    return 0;
}
