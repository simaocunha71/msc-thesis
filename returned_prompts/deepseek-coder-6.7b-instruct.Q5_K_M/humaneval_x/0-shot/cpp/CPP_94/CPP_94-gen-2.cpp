    int sum=0,max=0;
    for(int i=0;i<lst.size();i++){
        int count=0;
        for(int j=1;j<=lst[i];j++){
            if(lst[i]%j==0)
                count++;
        }
        if(count==2 && max<lst[i]){
            max=lst[i];
        }
    }
    while(max>0){
        sum+=max%10;
        max/=10;
    }
    return sum;
}

int main()
{
    vector<int> lst={0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3};
    printf("%d\n",skjkasdkd(lst));
    return 0;
}

//The function skjkasdkd(vector<int> lst) takes a vector of integers as an argument. It initializes sum and max to 0. Then it runs a loop through the vector, checking each number to see if it is prime and if it's greater than max. If it is, max is updated. After the loop, it runs another loop that adds the digits of max to sum and returns sum.
//The main function tests the function with the vector {0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3}.
//The output of the function should be 10.

//The function skjkasdkd(vector<int> lst) takes a vector of integers as an argument. It initializes sum and max to 0. Then it runs a loop through the vector, checking each number to see if it is prime and if it's greater than max. If it is, max is updated. After the loop, it runs another loop that adds the digits of max to sum and returns sum.
//The main function tests the function with the vector {