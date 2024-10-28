    sort(words.begin(), words.end());
    vector<int> unique_counts;
    for (auto word : words){
        sort(word.begin(), word.end());
        unique_counts.push_back(distance(word.begin(), unique(word.begin(), word.end())));
    }

B:
    int max_unique_count = *max_element(unique_counts.begin(), unique_counts.end());

C:
    for (int i = 0; i < unique_counts.size(); i++){
        if (unique_counts[i] == max_unique_count){
            return words[i];
        }
    }
}

int main() {
    printf("find_max({'name', 'of', 'string'}) = %s\n", find_max({"name", "of", "string"}).c_str());
    printf("find_max({'name', 'enam', 'game'}) = %s\n", find_max({"name", "enam", "game"}).c_str());
    printf("find_max({'aaaaaaa', 'bb', 'cc'}) = %s\n", find_max({"aaaaaaa", "bb", "cc"}).c_str());
    return 0;
}
*/

#include <string>
#include <vector>
#include <algorithm>

std::string find_max(std::vector<std::string> words) {
    std::sort(words.begin(), words.end());
    std::vector<int> unique_counts;
    for (const auto& word : words) {
        unique_counts.push_back(std::distance(word.begin(), std::unique(word.begin(), word.end())));
    }
    int max_unique_count = *std::max_element(unique_counts.begin(), unique_counts.end());
    for (const auto& word : words) {
        if (std::distance(word.begin(), std::unique(word.begin(), word.end())) == max_unique_count) {
            return word;
        }
    }
   