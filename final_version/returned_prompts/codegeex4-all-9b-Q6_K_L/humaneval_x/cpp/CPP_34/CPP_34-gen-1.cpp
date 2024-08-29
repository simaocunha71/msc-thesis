    sort(l.begin(), l.end());
    vector<int> res;
    for(int i = 0; i < l.size(); i++){
        if(i == 0 || l[i] != l[i-1]){
            res.push_back(l[i]);
        }
    }
    return res;

B:
    sort(l.begin(), l.end());
    vector<int> res;
    int i = 0;
    while(i < l.size()){
        res.push_back(l[i]);
        while(i < l.size() && l[i] == l[i+1]){
            i++;
        }
        i++;
    }
    return res;

C:
    sort(l.begin(), l.end());
    vector<int> res;
    int i = 0;
    while(i < l.size()){
        res.push_back(l[i]);
        while(i < l.size() && l[i] == l[i+1]){
            i++;
        }
        i++;
    }
    sort(res.begin(), res.end());
    return res;
}

int main(){
    vector<int> l = {5, 3, 5, 2, 3, 3, 9, 0, 123};
    vector<int> res = unique(l);
    for(int i = 0; i < res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}
请问哪个函数实现正确了？
A、B、C
A、B、C都正确
A、B、C都不正确
A、B正确
A、C正确
B、C正确
A、B都不正确
A、C都不正确
B、C都不正确
A正确，B、C不正确
B正确，A、C不正确
C正确，A、B不正确
A正确，B、C都不正确
B正确，A、C都不正确
C正确，A、B都不正确
A、B正确，C不正确
A、C正确，B不正确
B、C正确，A不正确
A、B、C都不正确
A正确，B正确，C不正确
B正确，A正确，C不正确
C正确，A正确，B不正确
A正确，B不正确，C不正确
B正确，A不正确，C不正确
C正确，A不正确，B不正确
A不正确，B正确，C不正确
B不正确，A正确