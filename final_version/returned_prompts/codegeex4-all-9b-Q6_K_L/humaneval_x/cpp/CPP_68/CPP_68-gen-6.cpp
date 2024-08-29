vector<int> pluck(vector<int> arr){
        if(arr.size() == 0){
            return {};
        }
        int min = arr[0];
        int minIndex = 0;
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] % 2 == 0 && arr[i] < min){
                min = arr[i];
                minIndex = i;
            }
        }
        if(min == arr[0]){
            return {};
        }
        return {min, minIndex};
    }

B:
vector<int> pluck(vector<int> arr){
        if(arr.size() == 0){
            return {};
        }
        int min = arr[0];
        int minIndex = 0;
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] % 2 == 0 && arr[i] <= min){
                min = arr[i];
                minIndex = i;
            }
        }
        return {min, minIndex};
    }

C:
vector<int> pluck(vector<int> arr){
        if(arr.size() == 0){
            return {};
        }
        int min = arr[0];
        int minIndex = 0;
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] % 2 == 0 && arr[i] < min){
                min = arr[i];
                minIndex = i;
            }
        }
        return {min, minIndex};
    }

D:
vector<int> pluck(vector<int> arr){
        if(arr.size() == 0){
            return {};
        }
        int min = arr[0];
        int minIndex = 0;
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] % 2 == 0 && arr[i] < min){
                min = arr[i];
                minIndex = i;
            }
        }
        return {min, minIndex};
    }

E:
vector<int> pluck(vector<int> arr){
        if(arr.size() == 0){
            return {};
        }
        int min = arr[0];
        int minIndex = 0;
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] % 2 == 0 && arr[i] <= min){
                min = arr[i];
                minIndex = i;
            }
        }
        return {min, min