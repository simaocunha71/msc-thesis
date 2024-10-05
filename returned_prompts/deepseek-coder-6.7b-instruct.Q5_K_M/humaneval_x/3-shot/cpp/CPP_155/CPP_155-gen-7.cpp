    vector<int> count(2,0); //initialize vector with 2 zeros
    num = abs(num); //to handle negative numbers
    while(num>0){
        int digit = num%10; //get last digit
        if(digit%2==0) 
            count[0]++;
        else 
            count[1]++;
        num = num/10; //remove last digit
    }
    return count;
}


