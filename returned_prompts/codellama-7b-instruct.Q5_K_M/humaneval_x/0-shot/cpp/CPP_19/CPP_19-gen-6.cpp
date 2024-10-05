
string s = numbers;
    stringstream ss(s);
    string temp;
    vector<int> nums;
    while (getline(ss, temp, ' '))
    {
        nums.push_back(atoi(temp.c_str()));
    }
    sort(nums.begin(), nums.end());
    stringstream oss;
    for(int i = 0; i < nums.size(); i++)
    {
        oss << nums[i] << " ";
    }
    oss >> numbers;
    return numbers;

}
int main()
{
    string str = "three one five";
    string ret = sort_numbers(str);
    cout << ret << endl;
    return 0;
}


