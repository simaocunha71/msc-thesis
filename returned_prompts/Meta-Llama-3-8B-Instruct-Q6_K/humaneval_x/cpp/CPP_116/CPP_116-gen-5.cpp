    vector<int> sorted_arr;

    for(int i = 0; i < arr.size(); i++){
        int ones = 0;
        int temp = arr[i];
        while(temp > 0){
            if(temp % 2 == 1) ones++;
            temp /= 2;
        }
        arr[i] = {ones, arr[i]};
    }

    sort(arr.begin(), arr.end());

    for(int i = 0; i < arr.size(); i++){
        arr[i] = arr[i].second;
    }

    return arr;
}

int main()
{
    vector<int> v = {1, 5, 2, 3, 4};
    vector<int> sorted = sort_array(v);
    for(int i = 0; i < sorted.size(); i++){
        cout << sorted[i] << " ";
    }
    return 0;
}

B:
    vector<int> sort_vector(vector<int> arr){
        sort(arr.begin(), arr.end(), [](int a, int b){
            int ones_a = 0, ones_b = 0;
            while(a > 0){
                if(a % 2 == 1) ones_a++;
                a /= 2;
            }
            while(b > 0){
                if(b % 2 == 1) ones_b++;
                b /= 2;
            }
            if(ones_a != ones_b) return ones_a < ones_b;
            else return a < b;
        });
        return arr;
    }

    int main()
    {
        vector<int> v = {1, 5, 2, 3, 4};
        vector<int> sorted = sort_vector(v);
        for(int i = 0; i < sorted.size(); i++){
            cout << sorted[i] << " ";
        }
        return 0;
    }
C:
    vector<int> sort_array(vector<int> arr){
        sort(arr.begin(), arr.end(), [](int a, int b){
            string a_bin = to_string(a), b_bin = to_string(b);
            int ones_a = 0, ones_b = 0;
            for(int i = 0; i < a_bin.size(); i++){
                if(a_bin[i] == '1') ones_a++;
            }
            for(int i = 0; i < b_bin.size(); i++){
                if(b_bin[i] == '1') ones_b++;
            }
            if(ones_a != ones_b) return