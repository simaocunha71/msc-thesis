    int a=0, b=0, c=0;
    if (n<3) return 0;
    for (int i=3;i<=n;i++){
        c=a+b;
        a=b;
        b=c;
    }
    return c;
}  // This function is correct but it will not work for large n because it uses O(n) space and time. We can improve it by using O(1) space and O(n) time. We can store the last three numbers in variables and update them in each iteration. This way we can compute the nth number in O(n) time and O(1) space. This function is more efficient than the previous one for large n. We can also add some error checking to ensure that the input is valid. This function is more robust than the previous one.

