    if(arr.empty())
        return {};

    int smallest_even = INT_MAX;
    int smallest_even_index = -1;

    for(int i = 0; i < arr.size(); i++)
    {
        if(arr[i]%2 == 0 && arr[i] < smallest_even)
        {
            smallest_even = arr[i];
            smallest_even_index = i;
        }
    }

    if(smallest_even == INT_MAX)
        return {};

    vector<int> result = {smallest_even, smallest_even_index};
    return result;
} 

int main()
{
    vector<int> arr = {4,2,3};
    vector<int> result = pluck(arr);
    for(auto it: result)
        printf("%d ", it);
    printf("\n");
    return 0;
}
B:
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;

    vector<int> pluck(vector<int>& arr) {
        vector<int> result;
        int smallest_even = INT_MAX;
        int smallest_even_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] % 2 == 0 && arr[i] < smallest_even) {
                smallest_even = arr[i];
                smallest_even_index = i;
            }
        }

        if (smallest_even == INT_MAX)
            return {};

        result.push_back(smallest_even);
        result.push_back(smallest_even_index);
        return result;
    }

    int main() {
        vector<int> arr = {4, 2, 3};
        vector<int> result = pluck(arr);
        for (auto it : result)
            cout << it << " ";
        cout << endl;
        return 0;
    }
C:
    #include <iostream>
    #include <vector>
    using namespace std;

    vector<int> pluck(vector<int>& arr) {
        vector<int> result;
        int smallest_even = INT_MAX;
        int smallest_even_index = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] % 2 == 0 && arr[i] < smallest_even) {
                smallest_even = arr[i];
                smallest_even_index = i;
            }
        }

        if (smallest_even == INT_MAX)
            return {};

        result = {smallest_even, smallest_even_index};
        return result;
