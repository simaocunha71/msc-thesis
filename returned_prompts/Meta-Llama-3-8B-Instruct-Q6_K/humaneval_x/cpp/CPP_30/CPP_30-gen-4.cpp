    vector<float> res;
    for(auto it=l.begin();it!=l.end();it++){
        if(*it>0)
            res.push_back(*it);
    }
    return res;
}
int main()
{
    vector<float> l = {-1,2,-4,5,6};
    vector<float> res = get_positive(l);
    for(auto it=res.begin();it!=res.end();it++)
        printf("%f ",*it);
    return 0;
}
B:
    #include <iostream>
    #include <vector>
    #include <algorithm>
    using namespace std;
    vector<float> get_positive(vector<float> l){
        vector<float> res;
        for(auto it=l.begin();it!=l.end();it++){
            if(*it>0)
                res.push_back(*it);
        }
        return res;
    }
    int main(){
        vector<float> l = {-1,2,-4,5,6};
        vector<float> res = get_positive(l);
        for(auto it=res.begin();it!=res.end();it++)
            cout << *it << " ";
        return 0;
    }
C:
    #include <iostream>
    #include <vector>
    using namespace std;
    vector<float> get_positive(vector<float> l){
        vector<float> res;
        for(auto it:l.begin();it!=l.end();it++){
            if(*it>0)
                res.push_back(*it);
        }
        return res;
    }
    int main(){
        vector<float> l = {-1,2,-4,5,6};
        vector<float> res = get_positive(l);
        for(auto it=res.begin();it!=res.end();it++)
            cout << *it << " ";
        return 0;
    }
D:
    #include <iostream>
    #include <vector>
    using namespace std;
    vector<float> get_positive(vector<float> l){
        vector<float> res;
        for(auto it=l.begin();it!=l.end();it++){
            if(*it>0)
                res.push_back(*it);
        }
        return res;
    }
    int main(){
        vector<float> l = {-1,2,-4,5,6};
        vector<float> res = get_positive(l);
        for(auto it=res.begin();it!=res.end();it++)
            cout << *it << endl;
        return 0;
    }
E:
    #include <iostream>
    #