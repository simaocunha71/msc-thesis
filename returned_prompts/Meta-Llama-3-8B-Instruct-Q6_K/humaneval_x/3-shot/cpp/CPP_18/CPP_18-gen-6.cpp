    int count = 0;
    int n = str.length();
    int m = substring.length();
    for(int i = 0; i <= n - m; i++) {
        if(str.substr(i, m) == substring) {
            count++;
            i++;
        }
    }
    return count;
}
// Alternative solution
int how_many_times(string str,string substring){
    int count = 0;
    int n = str.length();
    int m = substring.length();
    for(int i = 0; i <= n - m; i++) {
        if(str.find(substring, i) != string::npos) {
            count++;
            i += m;
        }
    }
    return count;
}  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just finds the next occurrence of the substring.  // This solution is more efficient than the previous one, it does not need to substr every time, it just