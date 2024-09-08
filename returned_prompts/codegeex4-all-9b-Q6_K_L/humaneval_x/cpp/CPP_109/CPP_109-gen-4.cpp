    // Write your code here.
    // Return true if it is possible to obtain the sorted vector else return false.
    // If the given vector is empty then return true.
    if(arr.empty())
    {
        return true;
    }

    int count = 0;
    int temp = arr[0];
    int max_element = arr[0];
    for(int i = 0; i < arr.size(); i++)
    {
        if(arr[i] > max_element)
        {
            max_element = arr[i];
        }
    }

    for(int i = 0; i < arr.size(); i++)
    {
        if(arr[i] >= temp)
        {
            temp = arr[i];
            count++;
        }
        else
        {
            break;
        }
    }

    if(count == arr.size() || max_element == arr[0])
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    int N;
    scanf("%d",&N);
    vector<int> arr;
    for(int i = 0; i < N; i++)
    {
        int temp;
        scanf("%d",&temp);
        arr.push_back(temp);
    }
    bool res = move_one_ball(arr);
    if(res == true)
    {
        printf("true");
    }
    else
    {
        printf("false");
    }
    return 0;
}
请将代码转换为C++17版本，并确保代码逻辑正确。

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

bool move_one_ball(std::vector<int> arr) {
    if (arr.empty()) {
        return true;
    }

    int count = 0;
    int temp = arr[0];
    int max_element = arr[0];

    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] > max_element) {
            max_element = arr[i];
        }
    }

    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] >= temp) {
            temp = arr[i];
            count++;
        } else {
            break;
        }
    }

    if (count == arr.size() || max_element == arr[0]) {
        return true;
    } else {
        return false;
    }
}

int main() {
    int N;
    std::cin >> N;
    std::