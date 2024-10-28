    int start = max(interval1[0], interval2[0]);
    int end = min(interval1[1], interval2[1]);
    if (start > end) return "NO";
    int len = end - start + 1;
    if (is_prime(len)) return "YES";
    return "NO";
}
bool is_prime(int n){
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0)
            return false;
    return true;
}  //end of is_prime() function
}  //end of namespace std.  //end of intersection() function

