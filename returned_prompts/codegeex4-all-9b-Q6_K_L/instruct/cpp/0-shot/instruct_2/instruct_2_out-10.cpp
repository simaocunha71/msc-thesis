    void sort_output_counts(const std::map<int, int>& anonymous_output_statistics,
                            const std::vector<int>& output_counts,
                            std::vector<int>& sorted_output_counts) {
        std::vector<std::pair<int, int>> output_statistics_pairs;

        for (const auto& pair : anonymous_output_statistics) {
            output_statistics_pairs.emplace_back(pair.second, pair.first);
        }

        std::sort(output_statistics_pairs.begin(), output_statistics_pairs.end(),
                  [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
                      if (a.first == b.first) {
                          return a.second < b.second;
                      }
                      return a.first > b.first;
                  });

        for (const auto& pair : output_statistics_pairs) {
            sorted_output_counts.push_back(output_counts[pair.second]);
        }
    }