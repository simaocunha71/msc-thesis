    sort(nums.begin(),nums.end(),[&](int a, int int b){
        if (abs(a)%10 != abs(b)%10) return abs(a)%10 < abs(b)%10;
        else return find(nums.begin(),nums.end(),a) < find(nums.begin(),nums.end(),b);
    });
    return nums;
}
//OR
#include<map>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    map<int,vector<int>> m;
    for(auto i:nums){
        m[abs(i)%10].push_back(i);
    }
    vector<int> res;
    for(auto i:m){
        for(auto j:i.second){
            res.push_back(j);
        }
    }
    return res;
}

//OR
#include<algorithm>
#include<vector>
#include<map>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    map<int,vector<int>> m;
    for(auto i:nums){
        m[abs(i)%10].push_back(i);
    }
    vector<int> res;
    for(auto i:m){
        for(auto j:i.second){
            res.push_back(j);
        }
    }
    sort(res.begin(),res.end());
    return res;
}
//OR
#include<algorithm>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    sort(nums.begin(),nums.end(),[&](int a, int int b){
        if (abs(a)%10 == abs(b)%10) return nums.find(a) < nums.find(b);
        else return abs(a)%10 < abs(b)%10;
    });
    return nums;
}
//OR
#include<map>
using namespace std;
vector<int> order_by_points(vector<int> nums){
    map<int,int> m;
    for(auto i:nums){
        m[abs(i)%10]++;
    }
    vector<int> res;
    for(auto i:m){
        for(int j=0;j<i.second;j++){
            res.push_back(i.first*10);
        }
    }
    sort(res.begin(),res.end());
    return res;
}

