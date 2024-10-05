
}

int main(){
    vector<string> lst1={"hi", "admin"};
    vector<string> lst2={"hI", "Hi"};
    vector<string> res=total_match(lst1,lst2);
    for(int i=0;i<res.size();i++)
        cout<<res[i]<<" ";
    return 0;
}



