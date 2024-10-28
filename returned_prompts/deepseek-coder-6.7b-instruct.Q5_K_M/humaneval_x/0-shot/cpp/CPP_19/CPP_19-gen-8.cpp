    map<string, string> num_map;
    num_map["zero"] = "0";
    num_map["one"] = "1";
    num_map["two"] = "2";
    num_map["three"] = "3";
    num_map["four"] = "4";
    num_map["five"] = "5";
    num_map["six"] = "6";
    num_map["seven"] = "7";
    num_map["eight"] = "8";
    num_map["nine"] = "9";

    stringstream ss(numbers);
    string word;
    vector<string> nums;

    while(ss >> word){
        nums.push_back(num_map[word]);
    }

    sort(nums.begin(), nums.end());

    string sorted_numbers = "";
    for(string num : nums){
        for(auto it=num_map.begin(); it != num_map.end(); ++it){
            if(it->second == num){
                if(sorted_numbers.size()>0)
                    sorted_numbers += " ";
                sorted_numbers += it->first;
                break;
            }
        }
    }

    return sorted_numbers;
}

int main()
{
    string numbers = "three one five";
    cout<<sort_numbers(numbers);
    return 0;
}

Output:
"one three five"
*/

int main()
{
    string numbers = "three one five";
    cout<<sort_numbers(numbers);
    return 0;
}

Output:
"one three five"
*/

int main()
{
    string numbers = "three one five";
    cout<<sort_numbers(numbers);
    return 0;
}

Output:
"one three five"
*/

int main()
{
    string numbers = "three one five";
    cout<<sort_numbers(numbers);
    return 0;
}

Output:
"one three five"
*/
