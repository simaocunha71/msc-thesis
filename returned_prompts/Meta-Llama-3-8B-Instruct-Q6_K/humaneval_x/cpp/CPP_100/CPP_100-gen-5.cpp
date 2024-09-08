    vector<int> stones;
    if(n <= 0) return stones;
    stones.push_back(n);
    for(int i = 1; i < n; i++){
        if(n % 2 == 0) stones.push_back(n + 1);
        else stones.push_back(n - 1);
        n = n - 1;
    }
    return stones;
}

B:
    vector<int> make_a_pile(int n){
        vector<int> stones;
        stones.push_back(n);
        while(n > 1){
            n = (n % 2 == 0) ? n - 1 : n + 1;
            stones.push_back(n);
        }
        return stones;
    }

C:
    vector<int> make_a_pile(int n){
        vector<int> stones;
        stones.push_back(n);
        while(n > 1){
            n = (n % 2 == 1) ? n - 1 : n + 1;
            stones.push_back(n);
        }
        return stones;
    }

D:
    vector<int> make_a_pile(int n){
        vector<int> stones;
        stones.push_back(n);
        while(n > 1){
            n = (n % 2 == 0) ? n + 1 : n - 1;
            stones.push_back(n);
        }
        return stones;
    }

E:
    vector<int> make_a_pile(int n){
        vector<int> stones;
        stones.push_back(n);
        while(n > 1){
            n = n % 2 ? n - 1 : n + 1;
            stones.push_back(n);
        }
        return stones;
    }

F:
    vector<int> make_a_pile(int n){
        vector<int> stones;
        stones.push_back(n);
        while(n > 1){
            n = (n & 1) ? n - 1 : n + 1;
            stones.push_back(n);
        }
        return stones;
    }

G:
    vector<int> make_a_pile(int n){
        vector<int> stones;
        stones.push_back(n);
        while(n > 1){
            n = n & 1 ? n - 1 : n + 1;
            stones.push_back(n);
        }
        return stones;
    }

H:
    vector<int> make_a_pile(int n){
        vector<int> stones;
        stones.push_back(n);
        while(n > 1){
