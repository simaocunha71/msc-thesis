    int count=0;
    for(int i=0; i<n.size(); i++){
        int sum=0;
        if(n[i]<0){
            int temp = abs(n[i]);
            while(temp){
                sum += -(temp%10);
                temp /= 10;
            }
        }
        else{
            int temp = n[i];
            while(temp){
                sum += temp%10;
                temp /= 10;
            }
        }
        if(sum>0) count++;
    }
    return count;
}
int main(){
    vector<int> n = {-1,11,-11};
    printf("%d\n", count_nums(n));
}

/*
The function count_nums takes a vector of integers as input. It iterates through the vector and for each number it calculates the sum of its digits. If the number is negative, it converts it to positive and calculates the sum of its digits, but adds the negative sign to each digit. If the sum of digits is positive, it increments the count. Finally it returns the count.
*/




//  I'm not sure if you're asking for the C++ version of the code, but the code is already in C++. If you're asking for a version in a different language, please provide more information.
//  I hope this helps you understand how the code works. If you have any further questions, feel free to ask.


























































































































































