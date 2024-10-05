    vector<int> nums = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> roman = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    string res = "";

B:
    for(int i = 0; i < nums.size(); i++){
        while(number >= nums[i]){
            res += roman[i];
            number -= nums[i];
        }
    }

C:
    return res;
}

int main(){
    printf("%s\n", int_to_mini_roman(19).c_str());
    printf("%s\n", int_to_mini_roman(152).c_str());
    printf("%s\n", int_to_mini_roman(426).c_str());
    return 0;
}
*/

