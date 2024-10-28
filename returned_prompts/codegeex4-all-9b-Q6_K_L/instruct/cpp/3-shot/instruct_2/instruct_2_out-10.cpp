    The code should be as short as possible, but still easy to understand.
    
```cpp
#include <map>
#include <vector>
#include <algorithm>

std::vector<int> sortOutputCounts(const std::map<int, std::map<int, int>>& outputStats, const std::vector<int>& outputCounts) {
    std::vector<int> sortedOutputCounts;
    for (const auto& outputStat : outputStats) {
        for (const auto& count : outputStat.second) {
            sortedOutputCounts.push_back(count.second);
        }
    }
    std::sort(sortedOutputCounts.begin(), sortedOutputCounts.end(), std::greater<int>());
    return sortedOutputCounts;
}
```