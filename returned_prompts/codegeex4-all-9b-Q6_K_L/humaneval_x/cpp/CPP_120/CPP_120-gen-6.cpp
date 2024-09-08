#include <bits/stdc++.h>
#include<queue>
using namespace std;
vector<int> maximum(vector<int> arr,int k){
    priority_queue<int> q;
    for(auto i:arr){
        q.push(i);
        if(q.size()>k){
            q.pop();
        }
    }
    vector<int> v;
    while(!q.empty()){
        v.push_back(q.top());
        q.pop();
    }
    reverse(v.begin(),v.end());
    return v;
}

B:
#include <bits/stdc++.h>
using namespace std;
vector<int> maximum(vector<int> arr,int k){
    priority_queue<int> q;
    for(auto i:arr){
        q.push(i);
        if(q.size()>k){
            q.pop();
        }
    }
    vector<int> v;
    while(!q.empty()){
        v.push_back(q.top());
        q.pop();
    }
    return v;
}

C:
#include<bits/stdc++.h>
#include<queue>
using namespace std;
vector<int> maximum(vector<int> arr,int k){
    priority_queue<int> q;
    for(int i=0;i<arr.size();i++){
        q.push(arr[i]);
        if(q.size()>k){
            q.pop();
        }
    }
    vector<int> v;
    while(!q.empty()){
        v.push_back(q.top());
        q.pop();
    }
    reverse(v.begin(),v.end());
    return v;
}

D:
#include <bits/stdc++.h>
#include<queue>
using namespace std;
vector<int> maximum(vector<int> arr,int k){
    priority_queue<int> q;
    for(int i:arr){
        q.push(i);
        if(q.size()>k){
            q.pop();
        }
    }
    vector<int> v;
    while(!q.empty()){
        v.push_back(q.top());
        q.pop();
    }
    reverse(v.begin(),v.end());
    return v;
}

E:
#include <bits/stdc++.h>
#include<queue>
using namespace std;
vector<int> maximum(vector<int> arr,int k){
    priority_queue<int> q;
    for(int i=0;i<arr.size();i++){
        q.push(arr[i]);
        if(q.size()>k){
            q.pop();
        }
    }
    vector<int> v;
    while(!q.empty()){
        v.push_back(q.top());
        q.pop();
    }
    return v;
}
F:
#include<bits/stdc++.h>
#include<queue>
using namespace std;
vector<int> maximum(vector