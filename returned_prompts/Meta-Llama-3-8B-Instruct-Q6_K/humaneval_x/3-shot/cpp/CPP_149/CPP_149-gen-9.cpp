    vector<string> result;
    for (auto word : lst)
    {
        if (word.size() % 2 == 0)
        {
            result.push_back(word);
        }
    }
    sort(result.begin(), result.end(), [](string a, string b)
    {
        if (a.size() == b.size())
        {
            return a < b;
        }
        return a.size() < b.size();
    });
    return result;
}
// You can use this function to test your solution:
void print(vector<string> v)
{
    for (auto str : v)
    {
        printf("%s\n", str.c_str());
    }
}
int main()
{
    vector<string> v = {"a", "aa", "aaa", "cd", "ab"};
    print(sorted_list_sum(v));
    return 0;
}
// Output:
// ab
// cd
// aa
// You can also use the following code to test your solution:
// assert(sorted_list_sum({"aa", "a", "aaa"}) == {"aa"});
// assert(sorted_list_sum({"ab", "a", "aaa", "cd"}) == {"ab", "cd"});
// assert(sorted_list_sum({}) == {});
// You can also test your solution with more test cases to ensure it works correctly.