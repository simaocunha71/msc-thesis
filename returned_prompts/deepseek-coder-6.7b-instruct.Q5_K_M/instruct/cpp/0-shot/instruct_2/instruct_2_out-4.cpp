    */

#include <map>
#include <vector>
#include <algorithm>

std::vector<int> sortOutputs(const std::map<std::string, int>& outputStats, const std::vector<int>& outputCounts) {
    std::vector<std::pair<int, std::string>> temp;
    for(auto& kv : outputStats) {
        temp.push_back(std::make_pair(outputCounts[kv.second], kv.first));
    }
    std::sort(temp.begin(), temp.end(), std::greater<>());
    std::vector<int> result;
    for(auto& kv : temp) {
        result.push_back(kv.second);
    }
    return result;
}

//src/SortOutputs/test.cpp
#include "sortOutputs.cpp"
#include <iostream>

int main() {
    std::map<std::string, int> outputStats = {{"output1", 0}, {"output2", 1}, {"output3", 2}};
    std::vector<int> outputCounts = {10, 20, 30};
    std::vector<int> sortedOutputs = sortOutputs(outputStats, outputCounts);
    for(int output : sortedOutputs) {
        std::cout << output << " ";
    }
    return 0;
}#include <iostream>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    int arr[n][m];

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            cin >> arr[i][j];
        }
    }

    int sum=0, maxSum=INT_MIN;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m;