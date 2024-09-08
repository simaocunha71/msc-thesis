vector<int> res;
while (n!=1){
    if (n%2==0) n/=2;
    else{
        res.push_back(n);
        n = 3*n + 1;
    }
}
res.push_back(1);
sort(res.begin(),res.end());
return res;

}

B:
vector<int> get_odd_collatz(int n){

vector<int> res;
while (n!=1){
    if (n%2==0) n/=2;
    else{
        res.push_back(n);
        n = 3*n + 1;
    }
}
res.push_back(1);
sort(res.begin(),res.end());
return res;

}

C:
vector<int> get_odd_collatz(int n){

vector<int> res;
while (n!=1){
    if (n%2==1){
        res.push_back(n);
        n = 3*n + 1;
    }
    else{
        n/=2;
    }
}
res.push_back(1);
sort(res.begin(),res.end());
return res;

}

D:
vector<int> get_odd_collatz(int n){

vector<int> res;
while (n!=1){
    if (n%2==1){
        res.push_back(n);
        n = 3*n + 1;
    }
    else{
        n/=2;
    }
}
res.push_back(1);
reverse(res.begin(),res.end());
return res;

}

E:
vector<int> get_odd_collatz(int n){

vector<int> res;
while (n!=1){
    if (n%2==1){
        res.push_back(n);
        n = 3*n + 1;
    }
    else{
        n/=2;
    }
}
res.push_back(1);
sort(res.begin(),res.end());
reverse(res.begin(),res.end());
return res;

}

F:
vector<int> get_odd_collatz(int n){

vector<int> res;
while (n!=1){
    if (n%2==1){
        res.push_back(n);
        n = 3*n + 1;
    }
    else{
        n/=2;
    }
}
res.push_back(1);
return res;

}

G:
vector<int> get_odd_collatz(int n){

vector<int> res;
while (n!=1){
    if (n%2==1){
        res.push_back(n);
        n = 3*n + 1;
    }
    else{
        n/=2;
        res.push_back