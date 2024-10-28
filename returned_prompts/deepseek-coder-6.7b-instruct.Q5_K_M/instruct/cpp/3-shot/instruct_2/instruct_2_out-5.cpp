        vector<pair<string, int>> output_counts;
        for(auto it = output_statistics.begin(); it != output_statistics.end(); ++it) {
            output_counts.push_back(make_pair(it->first, it->second));
        }
        
        sort(output_counts.begin(), output_counts.end(), [](const pair<string, int>& a, const pair<string, int>& b) {
            return a.second > b.second;  // Sort in descending order
        });
        
        for(auto it = output_counts.begin(); it != output_counts.end(); ++it) {
            cout << it->first << ": " << it->second << endl;
        }

