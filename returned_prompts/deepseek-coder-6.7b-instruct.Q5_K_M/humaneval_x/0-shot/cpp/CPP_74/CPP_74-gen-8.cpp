    int sum1 = 0, sum2 = 0;
    for(auto& i : lst1) sum1 += i.size();
    for(auto& i : lst2) sum2 += i.size();
    return sum1 < sum2 ? lst1 : lst2;
}

int main()
{
    vector<string> lst1 = {"hi", "admin"};
    vector<string> lst2 = {"hI", "Hi"};
    vector<string> ans = total_match(lst1, lst2);
    for(auto i : ans) printf("%s ", i.c_str());
}

Output:
hI Hi 

*/
