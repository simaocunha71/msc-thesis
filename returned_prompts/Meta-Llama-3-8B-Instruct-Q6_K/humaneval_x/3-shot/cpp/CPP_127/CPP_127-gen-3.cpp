    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if(start > end) return "NO";
    int length = end - start + 1;
    if(length <= 1) return "NO";
    for(int i = 2; i * i <= length; i++){
        if(length % i == 0) return "NO";
    }
    return "YES";
} 
// You can use this helper function to check if a number is prime or not.
bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
} 
// You can use this function to check if the length of the intersection is prime or not.
string intersection( vector<int> interval1,vector<int> interval2){
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if(start > end) return "NO";
    int length = end - start + 1;
    if(length <= 1) return "NO";
    return isPrime(length) ? "YES" : "NO";
} 
// You can use this function to check if the length of the intersection is prime or not.
string intersection( vector<int> interval1,vector<int> interval2){
    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if(start > end) return "NO";
    int length = end - start + 1;
    if(length <= 1) return "NO";
    return (isPrime(length)) ? "YES" : "NO";
}  // This function will return "YES" if the length of intersection is prime else it will return "NO".  // This function will return "YES" if the length of intersection is prime else it will return "NO".  // This function will return "YES" if the length of intersection is prime else it will return "NO".  // This function will return "YES" if the length of intersection is prime else it will return "NO".  // This function will return "YES" if the length of intersection is prime else it will return "NO". 