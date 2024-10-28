    vector<int> result;
    if(l1.size()>l2.size()){
        for(int i=0;i<l2.size();i++){
            if(l1.size()==0)
                return result;
            if(l2[i]==l1[0]){
                result.push_back(l2[i]);
                for(int j=0;j<l1.size();j++)
                    l1[j]--;
                goto A;
            }
        }
    }else{
        for(int i=0;i<l1.size();i++){
            if(l2.size()==0)
                return result;
            if(l1[i]==l2[0]){
                result.push_back(l1[i]);
                for(int j=0;j<l2.size();j++)
                    l2[j]--;
                goto A;
            }
        }
    }
    return result;
}

int main(){
    vector<int> a,b;
    a.push_back(1);
    a.push_back(4);
    a.push_back(3);
    a.push_back(34);
    a.push_back(653);
    a.push_back(2);
    a.push_back(5);
    b.push_back(5);
    b.push_back(7);
    b.push_back(1);
    b.push_back(5);
    b.push_back(9);
    b.push_back(653);
    b.push_back(121);
    vector<int> c;
    c.push_back(5);
    c.push_back(3);
    c.push_back(2);
    c.push_back(8);
    vector<int> d;
    d.push_back(3);
    d.push_back(2);
    vector<int> e = common(a,b);
    vector<int> f = common(