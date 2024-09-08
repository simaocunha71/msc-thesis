    // Step 1: Calculate sum of digits for each number
    vector<pair<int, int>> points;
    for(int i=0; i<nums.size(); i++){
        int sum = 0;
        int num = nums[i];
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        points.push_back({sum, i});
    }

    // Step 2: Sort the points based on sum of digits and index
    sort(points.begin(), points.end());

    // Step 3: Create the result vector
    vector<int> result;
    for(int i=0; i<points.size(); i++){
        result.push_back(nums[points[i].second]);
    }

    return result;
}  // Step 4: Return the result vector

C:
    int main() {
        vector<int> nums = {1, 11, -1, -11, -12};
        vector<int> result = order_by_points(nums);
        for(int i=0; i<result.size(); i++){
            printf("%d ", result[i]);
        }
        printf("\n");
        return 0;
    }

O:
    Expected output:
    -1 -11 -12 1 11

    The above code sorts the vector of integers in ascending order based on the sum of their digits. If there are several items with similar sum of their digits, it orders them based on their index in the original vector. The code works by first calculating the sum of digits for each number, then sorting the points based on the sum of digits and index, and finally creating the result vector. The output of the code is the sorted vector of integers.  // Step 1: Calculate sum of digits for each number
    vector<pair<int, int>> points;
    for(int i=0; i<nums.size(); i++){
        int sum = 0;
        int num = nums[i];
        while(num > 0){
            sum += num % 10;
            num /= 10;
        }
        points.push_back({sum, i});
    }

    // Step 2: Sort the points based on sum of digits and index
    sort(points.begin(), points.end());

    // Step 3: Create the result vector
    vector<int> result;
    for(int i=0; i<points.size(); i++){
        result.push_back(nums[points[i].second]);
    }

    return result;
}