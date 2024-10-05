    int sum=0;
    int product=1;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        product*=numbers[i];
    }
    return vector<int> {sum, product};
}   // Corrected the code to return a vector of int
// vector<int> sum_product(vector<int> numbers){
//     int sum=0;
//     int product=1;
//     int i;
//     for (i=0;i<numbers.size();i++)
//     {
//         sum+=numbers[i];
//         product*=numbers[i];
//     }
//     return {sum, product};
// }   // The above code also works fine
// return vector<int> {sum, product};   // Corrected the code to return a vector of int


