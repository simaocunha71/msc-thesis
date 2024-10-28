    #include <vector>
    #include <map>
    #include <algorithm>

    using namespace std;

    vector<int> sortOutputCounts(map<string, int> output_stats, vector<string> output_counts) {
        vector<pair<string, int>> sort_counts;
        vector<int> result;

        for(auto &out : output_counts) {
            sort_counts.push_back(make_pair(out, output_stats[out]));
        }

        sort(sort_counts.begin(), sort_counts.end(), [](const pair<string, int> &a, const pair<string, int> &b) {
            return a.second > b.second;
        });

        for(auto &count : sort_counts) {
            result.push_back(count.second);
        }

        return result;
    }
