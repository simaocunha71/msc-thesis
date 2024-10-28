    /*
    Roman numeral:
    I 1
    V 5
    X 10
    L 50
    C 100
    D 500
    M 1000
    */
    int x = 1;
    vector<int> nums = {1000, 500, 100, 50, 10, 5, 1};
    vector<char> romans = {'M', 'D', 'C', 'L', 'X', 'V', 'I'};
    vector<char> roman_num;
    while(number > 0){
        for(int i = 0; i < nums.size(); ++i){
            int times = number / nums[i];
            number %= nums[i];
            if(times > 0){
                while(times--){
                    roman_num.push_back(romans[i]);
                }
                number -= nums[i];
                break;
            }
        }
    }
    string ans = "";
    for(int i = 0; i < roman_num.size(); ++i){
        ans += roman_num[i];
    }
    return ans;
}
int main(){
    int number = 19;
    cout << int_to_mini_romank(number) << endl;
    return 0;
}
