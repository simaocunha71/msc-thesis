        std::vector<std::pair<int, int>> outputCounts;
        for (const auto& stat : stats) {
            outputCounts.emplace_back(stat.second, 0);
        }
        for (const auto& count : counts) {
            if (outputCounts.size() > 0 && outputCounts[0].first == 0) {
                outputCounts[0].second += count;
            } else {
                outputCounts.emplace_back(0, count);
            }
        }
        std::sort(outputCounts.begin(), outputCounts.end(),
                  [](const auto& a, const auto& b) {
                      return a.second > b.second;
                  });
        for (auto& count : outputCounts) {
            std::cout << count.second << std::endl;
        }