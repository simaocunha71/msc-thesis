    map<string, int> num_map;
    num_map["zero"]=0;
    num_map["one"]=1;
    num_map["two"]=2;
    num_map["three"]=3;
    num_map["four"]=4;
    num_map["five"]=5;
    num_map["six"]=6;
    num_map["seven"]=7;
    num_map["eight"]=8;
    num_map["nine"]=9;
    string result;
    for (auto& it: numbers)
    {
        for (auto& x: num_map)
        {
            if (it==x.first)
            {
                result+=x.first+" ";
                break;
            }
        }
    }
    return result;
}  // This solution is incorrect. It does not sort the numbers. It just separates the numbers from the input string.
// To sort the numbers, we can use a sorting algorithm like bubble sort or quick sort. Here is the correct solution using bubble sort:
string sort_numbers(string numbers)
{
    vector<string> num_list;
    map<string, int> num_map;
    num_map["zero"]=0;
    num_map["one"]=1;
    num_map["two"]=2;
    num_map["three"]=3;
    num_map["four"]=4;
    num_map["five"]=5;
    num_map["six"]=6;
    num_map["seven"]=7;
    num_map["eight"]=8;
    num_map["nine"]=9;
    for (auto& it: numbers)
    {
        for (auto& x: num_map)
        {
            if (it==x.first)
            {
                num_list.push_back(x.first);
                break;
            }
        }
    }
    for (int i = 0; i < num_list.size(); i++) {
        for (int j = i + 1; j < num_list.size(); j++) {
            if (num_map[num_list[i]] > num_map[num_list[j]]) {
                string temp = num_list[i];
                num_list[i] = num_list[j];
                num_list[j] = temp;
            }
        }
    }
    string result;
    for (auto& it: num_list)
    {
        result+=it+" ";
    }
    return result;
}  // This solution is still incorrect. It does not handle the case where the input string is empty. It should return an empty string in this case. Here is the corrected solution:
string sort_numbers(string numbers)
{
