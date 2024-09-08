    vector<int> res;
    res.push_back(n);
    int i = 1;
    while(n > 0){
        if(n % 2 == 0){
            res.push_back(res.back() + 2);
            n -= res.back();
        }
        else{
            res.push_back(res.back() + 1);
            n -= res.back();
        }
    }
    return res;
}

B:
    vector<int> make_a_pile(int n) {
        vector<int> res;
        res.push_back(n);
        int i = 1;
        while(n > 0){
            if(n % 2 != 0)
                res.push_back(res.back() + 1);
            else
                res.push_back(res.back() + 2);
            n -= res.back();
        }
        return res;
    }

C:
    vector<int> make_a_pile(int n) {
        vector<int> res;
        res.push_back(n);
        int i = 1;
        while(n > 0){
            if(n % 2 == 0)
                res.push_back(res.back() + 2);
            else
                res.push_back(res.back() + 1);
            n -= res.back();
        }
        return res;
    }

D:
    vector<int> make_a_pile(int n) {
        vector<int> res;
        res.push_back(n);
        while(n > 0){
            if(n % 2 == 0)
                res.push_back(res.back() + 2);
            else
                res.push_back(res.back() + 1);
            n -= res.back();
        }
        return res;
    }

E:
    vector<int> make_a_pile(int n) {
        vector<int> res;
        res.push_back(n);
        while(n > 0){
            if(n % 2 == 0)
                n--;
            res.push_back(res.back() + 1);
            n--;
        }
        return res;
    }
F:
    vector<int> make_a_pile(int n) {
        vector<int> res;
        res.push_back(n);
        while(n > 0){
            if(n % 2 != 0)
                res.push_back(res.back() + 1);
            else
                res.push_back(res.back() + 2);
            n -= res.back();
        }
        return res;
    }

G:
    vector<int> make_a_pile(int n) {
        vector<int>