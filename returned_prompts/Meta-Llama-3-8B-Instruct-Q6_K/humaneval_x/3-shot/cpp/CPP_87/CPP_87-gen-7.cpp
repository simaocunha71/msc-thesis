    vector<vector<int>> result;
    for (int i=0; i<lst.size(); i++)
    {
        for (int j=0; j<lst[i].size(); j++)
        {
            if (lst[i][j]==x)
            {
                result.push_back({i, j});
            }
        }
    }
    sort(result.begin(), result.end());
    return result;
}  // Sort by row first, then by column in descending order
// sort(result.begin(), result.end(), [](const auto& a, const auto& b) {
//     if(a[0] == b[0]) {
//         return a[1] > b[1];
//     }
//     return a[0] < b[0];
// });  // Sort by row first, then by column in descending order
// return result;
}  // Sort by row first, then by column in descending order
// sort(result.begin(), result.end(), [](const auto& a, const auto& b) {
//     if(a[0] == b[0]) {
//         return a[1] > b[1];
//     }
//     return a[0] < b[0];
// });  // Sort by row first, then by column in descending order
// return result;  // Sort by row first, then by column in descending order
// sort(result.begin(), result.end(), [](const auto& a, const auto& b) {
//     if(a[0] == b[0]) {
//         return a[1] > b[1];
//     }
//     return a[0] < b[0];
// });  // Sort by row first, then by column in descending order
// return result;  // Sort by row first, then by column in descending order
// sort(result.begin(), result.end(), [](const auto& a, const auto& b) {
//     if(a[0] == b[0]) {
//         return a[1] > b[1];
//     }
//     return a[0] < b[0];
// });  // Sort by row first, then by column in descending order
// return result;  // Sort by row first, then by column in descending order
// sort(result.begin(), result.end(), [](const auto& a, const auto& b) {
//     if(a[0] == b[0]) {
//         return a[