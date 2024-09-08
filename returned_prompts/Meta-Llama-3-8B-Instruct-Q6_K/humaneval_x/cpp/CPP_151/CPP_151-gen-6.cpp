long long sum = 0;
for(float num : lst){
    if(num > 0 && num == (int)num){ // check if number is positive and integer
        if(num % 2 != 0){ // check if number is odd
            sum += pow(num, 2); // add square of number to sum
        }
    }
}
return sum; // return sum
}

