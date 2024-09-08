    int max_count = 0;
    string result;
    for(const auto& word : words){
        int count = 0;
        set<char> s;
        for(char c : word){
            s.insert(c);
            count++;
        }
        if(count > max_count){
            max_count = count;
            result = word;
        }
        else if(count == max_count){
            if(word < result){
                result = word;
            }
        }
    }
    return result;

} // end of function find_max
int main()
{
    vector<string> words = {"name", "of", "string"};
    printf("%s\n", find_max(words).c_str());
    return 0;
} // end of main


