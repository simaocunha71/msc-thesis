        std::vector<std::pair<int, int>> outstats;
        outstats.reserve(stats_map.size());
        for (auto const& i : stats_map) {
            outstats.emplace_back(i.first, i.second);
        }
        std::sort(outstats.begin(), outstats.end(), [](std::pair<int, int> const& a, std::pair<int, int> const& b) {
            return a.second > b.second;
        });
        std::vector<int> outcounts;
        outcounts.reserve(stats_map.size());
        for (auto const& i : outstats) {
            for (auto const& j : out_counts) {
                if (i.first == j.first) {
                    outcounts.push_back(j.second);
                    break;
                }
            }
        }
        std::sort(outcounts.begin(), outcounts.end(), [](int const& a, int const& b) {
            return a < b;
        });
        return outcounts;

