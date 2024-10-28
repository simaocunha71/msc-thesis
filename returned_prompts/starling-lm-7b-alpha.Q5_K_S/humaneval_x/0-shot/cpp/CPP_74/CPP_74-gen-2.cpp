    int i=0;
    int j=0;
    int c1=0;
    int c2=0;
    for(i=0;i<lst1.size();i++){
        for(j=0;j<lst2.size();j++){
            c1=lst1[i].size();
            c2=lst2[j].size();
            if(c1<c2){
                break;
            }
        }
        if(c1>c2){
            break;
        }
    }
    vector<string> v;
    for(i=0;i<lst1.size();i++){
        for(j=0;j<lst2.size();j++){
            if(i!=j){
                v.push_back(lst1[i]);
            }
        }
    }
    for(i=0;i<lst2.size();i++){
        if(c1>c2){
            v.push_back(lst2[i]);
        }
    }
    return v;
}

int main()
{
    vector<string> a;
    vector<string> b;
    vector<string> c;
    a.push_back("hi");
    a.push_back("admin");
    b.push_back("hI");
    b.push_back("Hi");
    c=total_match(a,b);
    int i;
    for(i=0;i<c.size();i++){
        printf("%s ",c[i]);
    }
    return 0;
}



































































































































