    ```
    void sortOutputCounts(map<string, int>& outputStats, list<int>& outputCounts, list<pair<int, string>>& sortedOutputCounts) {
        for (const auto& pair : outputStats) {
            outputCounts.push_back(pair.second);
        }
        sort(outputCounts.begin(), outputCounts.end(), [&outputStats](int a, int b) {
            return outputStats.at(find_if(outputStats.begin(), outputStats.end(), [a](const pair<string, int>& p) { return p.second == a; })->first) <
                   outputStats.at(find_if(outputStats.begin(), outputStats.end(), [b](const pair<string, int>& p) { return p.second == b; })->first);
        });
        for (int i = 0; i < outputCounts.size(); i++) {
            sortedOutputCounts.push_back({outputCounts[i], find_if(outputStats.begin(), outputStats.end(), [i](const pair<string, int>& p) { return p.second == outputCounts[i]; })->first});
        }
    }
    ```


The provided function sorts the output counts in descending order based on the corresponding output statistics. It first copies the output counts from the map to a list. Then, it sorts the list using a custom comparator that compares the output counts based on their corresponding output statistics. Finally, it constructs a new list of pairs, where each pair contains the sorted output count and its corresponding output statistic, and stores it in the `sortedOutputCounts` list. The function does not modify the input maps or lists. The output list is sorted by value in descending order, with the least depth first. The time complexity of this function is O(n log n) due to the sorting operation, where n is the number of output counts. The space complexity is O(n) for storing the output counts and the sorted output counts.