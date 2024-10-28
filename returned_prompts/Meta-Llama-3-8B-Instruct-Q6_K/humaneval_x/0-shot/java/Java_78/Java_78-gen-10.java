    int count = 0;
    for(int i = 0; i < num.length(); i++){
        char c = num.charAt(i);
        if(c >= '2' && c <= '9' || c == 'B' || c == 'D' || c == 'F'){
            if(isPrime(Integer.parseInt(String.valueOf(c), 16))){
                count++;
            }
        }
    }
    return count;
}

private boolean isPrime(int n) {
    if(n <= 1) return false;
    if(n == 2) return true;
    if(n % 2 == 0) return false;
    int sqrt = (int)Math.sqrt(n);
    for(int i = 3; i <= sqrt; i+=2) {
        if(n % i == 0) return false;
    }
    return true;
}