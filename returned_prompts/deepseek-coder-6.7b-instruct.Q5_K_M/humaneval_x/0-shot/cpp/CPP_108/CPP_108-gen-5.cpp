    int sum=0;
    int count=0;
    for(int i=0; i<n.size(); i++){
        sum=0;
        if(n[i]<0){
            n[i]=n[i]*-1;
            while(n[i]>0){
                sum += n[i]%10;
                n[i] /= 10;
            }
            sum *= -1;
        }
        else{
            while(n[i]>0){
                sum += n[i]%10;
                n[i] /= 10;
            }
        }
        if(sum>0){
            count++;
        }
    }
    return count;
}

int main(){
    vector<int> nums={1,1,2};
    printf("%d\n", count_nums(nums));
    return 0;
}

Note: This solution assumes that the input vector "n" only contains integers.
*/

//Answer:
/*
The function count_nums checks each number in the given vector. If the number is negative, it multiplies it by -1 to treat the first digit as signed. Then, it calculates the sum of its digits by continuously dividing the number by 10 and adding the remainder (which is the last digit). If the sum of the digits is greater than 0, the count is incremented by 1. Finally, the function returns the count.
*/

//Explanation:
/*
Let's consider the example vector {1, 1, 2}. 
The first number 1 has a sum of digits 1 which is > 0, so the count is 1. 
The second number 1 has a sum of digits 1 which is > 0, so the count becomes 2. 
The third number 2 has a sum of digits 2 which is > 0, so the count becomes 3. 
So, the function count_nums returns 3.
*/

//Time Complexity:
/*
The time complexity of this solution is O(n*m), where n is the number of elements in the vector and