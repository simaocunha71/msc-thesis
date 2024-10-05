    vector<int> result;
    for(int i = 0; i < x.size(); i++){
        if(!(x[i] % 2 == 0)){
            int num = x[i];
            while(num){
                if(num % 10 % 2 != 0){
                    result.push_back(x[i]);
                    goto A;
                }
                num /= 10;
            }
        }
    }
    sort(result.begin(), result.end());
    return result;
}


/*
Given a vector of positive integers x. return a sorted vector of all 
elements that hasn't any even digit.

Note: Returned vector should be sorted in increasing order.

For example:
>>> unique_digits({15, 33, 1422, 1})
{1, 15, 33}
>>> unique_digits({152, 323, 1422, 10})
{}
*/

int main()
{
    vector<int> x = {15, 33, 1422, 1};
    vector<int> y = unique_digits(x);
    for(int i = 0; i < y.size(); i++){
        printf("%d ", y[i]);
    }
    return 0;
}















































































































































































