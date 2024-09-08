#include <iostream>
#include <vector>
#include <string>
using namespace std;
int specialFilter(vector<int> nums){
    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10){
            string str = to_string(nums[i]);
            if(str[0] % 2 != 0 && str[str.length() - 1] % 2 != 0){
                count++;
            }
        }
    }
    return count;
}
int main(){
    vector<int> nums1 = {15, -73, 14, -15};
    vector<int> nums2 = {33, -2, -3, 45, 21, 109};

    cout << "specialFilter({15, -73, 14, -15}) => " << specialFilter(nums1) << endl;
    cout << "specialFilter({33, -2, -3, 45, 21, 109}) => " << specialFilter(nums2) << endl;

    return 0;
}
B:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isSpecial(int num){
    string str = to_string(num);
    if(str.length() < 2){
        return false;
    }
    if(str[0] % 2 == 0 || str[str.length() - 1] % 2 == 0){
        return false;
    }
    return true;
}

int specialFilter(vector<int> nums){
    int count = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] > 10 && isSpecial(nums[i])){
            count++;
        }
    }
    return count;
}

int main(){
    vector<int> nums1 = {15, -73, 14, -15};
    vector<int> nums2 = {33, -2, -3, 45, 21, 109};

    cout << "specialFilter({15, -73, 14, -15}) => " << specialFilter(nums1) << endl;
    cout << "specialFilter({33, -2, -3, 45, 21, 109}) => " << specialFilter(nums2) << endl;

    return 0;
}
C:
#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool isSpecial(int num){
    string str = to_string