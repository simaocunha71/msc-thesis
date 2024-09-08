int can_arrange(vector<int> arr){
    int n = arr.size();
    int maxIndex = -1;
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i-1]) {
            maxIndex = i-1;
        }
    }
    return maxIndex;
}

B:
int can_arrange(vector<int> arr){
    int n = arr.size();
    int maxIndex = -1;
    for (int i = 0; i < n-1; i++) {
        if (arr[i] < arr[i+1]) {
            maxIndex = i;
        }
    }
    return maxIndex;
}

C:
int can_arrange(vector<int> arr){
    int n = arr.size();
    int maxIndex = -1;
    for (int i = 1; i < n; i++) {
        if (arr[i] > arr[i-1]) {
            maxIndex = i-1;
        }
    }
    return maxIndex;
}

D:
int can_arrange(vector<int> arr){
    int n = arr.size();
    int maxIndex = -1;
    for (int i = 0; i < n-1; i++) {
        if (arr[i] > arr[i+1]) {
            maxIndex = i;
        }
    }
    return maxIndex;
}

E:
int can_arrange(vector<int> arr){
    int n = arr.size();
    int maxIndex = -1;
    for (int i = 1; i < n; i++) {
        if (arr[i] > arr[i-1]) {
            maxIndex = i;
        }
    }
    return maxIndex;
}

F:
int can_arrange(vector<int> arr){
    int n = arr.size();
    int maxIndex = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] < arr[i+1]) {
            maxIndex = i;
        }
    }
    return maxIndex;
}

G:
int can_arrange(vector<int> arr){
    int n = arr.size();
    int maxIndex = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] < arr[i-1]) {
            maxIndex = i;
        }
    }
    return maxIndex;
}

H:
int can_arrange(vector<int>