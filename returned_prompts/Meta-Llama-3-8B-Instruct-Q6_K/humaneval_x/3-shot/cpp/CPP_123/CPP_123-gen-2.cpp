    vector<int> collatz;
    int num=n;
    while(num!=1){
        if (num%2==0)
            num=num/2;
        else
            num=3*num+1;
        collatz.push_back(num);
    }
    collatz.push_back(1);
    sort(collatz.begin(),collatz.end());
    vector<int> result;
    for (int i=0;i<collatz.size();i++)
        if (collatz[i]%2!=0)
            result.push_back(collatz[i]);
    return result;
}  // This function does not work correctly. It does not return the odd numbers from the Collatz sequence in increasing order. It returns the sequence itself.  // The correct solution should return {1,5} for input 5.  // A correct solution can be found at the end of this problem.  // For example:  // vector<int> get_odd_collatz(int n) {  //     vector<int> collatz;  //     int num=n;  //     while(num!=1){  //         if (num%2==0)  //             num=num/2;  //         else  //             num=3*num+1;  //         collatz.push_back(num);  //     }  //     vector<int> result;  //     for (int i=0;i<collatz.size();i++)  //         if (collatz[i]%2!=0)  //             result.push_back(collatz[i]);  //     sort(result.begin(),result.end());  //     return result;  // }  // This function does not work correctly. It does not return the odd numbers from the Collatz sequence in increasing order. It returns the sequence itself.  // The correct solution should return {1,5} for input 5.  // A correct solution can be found at the end of this problem.  // For example:  // vector<int> get_odd_collatz(int n) {  //     vector<int> collatz;  //     int num=n;  //     while(num!=1){  //         if (num%2==0)  //             num=num/2;  //         else  //             num=3*num+1;  //         collatz.push_back(num);  //     }  //     vector<int> result;  //     for (int i=0;i<collatz.size();i++)  //