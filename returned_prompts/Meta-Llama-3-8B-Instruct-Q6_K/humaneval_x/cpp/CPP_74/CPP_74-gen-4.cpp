    int sum1=0, sum2=0;
    for(auto str:lst1){
        sum1+=str.size();
    }
    for(auto str:lst2){
        sum2+=str.size();
    }
    if(sum1<sum2){
        return lst1;
    }else if(sum2<sum1){
        return lst2;
    }else{
        return lst1;
    }
}
int main() {
    vector<string> lst1 = {"hi", "admin"};
    vector<string> lst2 = {"hI", "Hi"};
    vector<string> result = total_match(lst1, lst2);
    for(auto str:result){
        cout<<str<<endl;
    }
    return 0;
} 

Output:
hI
Hi

Explanation:
The total_match function takes two vectors of strings as input. It calculates the total number of characters in each vector by summing up the sizes of all strings in the vector. It then compares the sums and returns the vector with the smaller sum. If the sums are equal, it returns the first vector. The function works correctly for the given examples. In the main function, we test the function with the example given in the problem statement and print the result. The output is as expected.