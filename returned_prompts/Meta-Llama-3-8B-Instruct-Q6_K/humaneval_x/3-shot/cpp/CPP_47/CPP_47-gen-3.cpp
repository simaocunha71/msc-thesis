    sort(l.begin(),l.end());
    int n=l.size();
    if (n%2==0) return (l[n/2-1]+l[n/2])/2.0;
    else return l[n/2];
}
//Note: This function assumes that the input vector l is not empty.
//If l is empty, it will throw an exception when trying to access l[0].
//If you want to handle the case where l is empty, you could add a check at the beginning of the function.
//For example: if (l.empty()) return 0.0;  // or some other default value for the median
//However, this is a matter of style and depends on the specific requirements of your program.