    int count = 0;
    string::size_type start = 0;
    while ((start = str.find(substring, start)) != string::npos) {
        ++count;
        start += 1; 
    }
    return count;
}
int main() {
    printf("%d\n",how_many_times("","a"));
    printf("%d\n",how_many_times("aaa","a"));
    printf("%d\n",how_many_times("aaaa","aa"));
    return 0;
}


A: The provided solution is correct, but it's using C++ standard library, not just C. If you want to stick to C, here is your solution.
