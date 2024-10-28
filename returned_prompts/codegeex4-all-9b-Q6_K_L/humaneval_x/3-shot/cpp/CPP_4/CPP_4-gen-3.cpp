
I'll try to review your code and provide comments on how to improve it.
has_close_elements
There's no need to use labels, nor to use goto.  Labels and goto are not good coding practices, and should be avoided whenever possible.
You can simplify your code by using std::next:
bool has_close_elements(vector<float> numbers, float threshold){
    for (auto i = numbers.begin(); i != numbers.end(); ++i) {
        for (auto j = std::next(i); j != numbers.end(); ++j) {
            if (std::abs(*i - *j) < threshold) {
                return true;
            }
        }
    }
    return false;
}

separate_paren_groups
You can simplify your code by using std::string::find and std::string::substr:
vector<string> separate_paren_groups(string paren_string){
    paren_string.erase(std::remove_if(paren_string.begin(), paren_string.end(), ::isspace), paren_string.end());
    vector<string> all_parens;
    size_t pos = 0;
    while (pos != std::string::npos) {
        pos = paren_string.find_first_of('(', pos);
        if (pos != std::string::npos) {
            size_t end = paren_string.find_first_of(')', pos);
            if (end != std::string::npos) {
                all_parens.push_back(paren_string.substr(pos, end - pos + 1));
                ++pos;
            }
        }
    }
    return all_parens;
}

truncate_number
You can simplify your code by using std::modf:
float truncate_number(float number){
    int integer;
    return std::modf(number, &integer);
}

mean_absolute_deviation
You can simplify your code by using std::accumulate:
float mean_absolute_deviation(vector<float> numbers){
    float sum = std::accumulate(numbers.begin(), numbers.end(), 0.0f);
    float mean = sum / numbers.size();
    return std::accumulate(numbers.begin(), numbers.end(), 0.0f, [&mean](float a, float