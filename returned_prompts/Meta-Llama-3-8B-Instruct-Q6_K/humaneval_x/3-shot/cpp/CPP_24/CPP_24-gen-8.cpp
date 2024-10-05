    for(int i=n-1; i>0; i--){
        if(n%i==0){
            return i;
        }
    }
    return 0;
} // This function will return 0 if no divisor is found, which should not happen for positive n. A more correct version would check for n > 0 before starting the loop.


