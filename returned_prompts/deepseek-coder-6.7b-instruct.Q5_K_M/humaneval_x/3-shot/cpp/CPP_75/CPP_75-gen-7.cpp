    int count = 0; 
    for(int i = 2; i*i <= a; i++) { 
        while(a % i == 0) { 
            if(i % 2 == 0) return false;
            a /= i;
            count++; 
        } 
    }
    if(a % 2 == 0) return false; 
    if(a > 1) count++; 
    return count == 3;
}


