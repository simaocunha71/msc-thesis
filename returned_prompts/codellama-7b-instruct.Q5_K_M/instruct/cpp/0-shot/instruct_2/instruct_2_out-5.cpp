
    std::vector<int> get_anon_output_counts(const map<int, int>& anon_output_stats,
                                           const vector<int>& output_counts)
    {
        vector<int> anon_output_counts;
        for (const auto& it : anon_output_stats)
        {
            int count = it.second;
            if (count > 0)
            {
                anon_output_counts.push_back(count);
            }
        }
        std::sort(anon_output_counts.begin(), anon_output_counts.end(),
                  [](int a, int b) { return a > b; });
        return anon_output_counts;
    }

