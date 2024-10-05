    vector<int> result;
    for (int num : x)
    {
        int is_valid = 1;
        while(num>0)
        {
            if(num%10 % 2 == 0)
            {
                is_valid = 0;
                break;
            }
            num /= 10;
        }
        if(is_valid)
        {
            result.push_back(num);
        }
    }
    sort(result.begin(),result.end());
    return result;
}
// or 
#include<vector>
#include<algorithm>
using namespace std;
vector<int> unique_digits(vector<int> x){
    vector<int> result;
    for (int num : x)
    {
        int is_valid = 1;
        while(num>0)
        {
            if(num%10 % 2 == 0)
            {
                is_valid = 0;
                break;
            }
            num /= 10;
        }
        if(is_valid)
        {
            result.push_back(num);
        }
    }
    sort(result.begin(),result.end());
    return result;
}  
// or 
#include<vector>
#include<algorithm>
using namespace std;
vector<int> unique_digits(vector<int> x){
    vector<int> result;
    for (int num : x)
    {
        if(all_of( begin( std::to_string(num) ), end( std::to_string(num) ), [](char c){ return c % 2 == 0; }))
            continue;
        result.push_back(num);
    }
    sort(result.begin(),result.end());
    return result;
}  



