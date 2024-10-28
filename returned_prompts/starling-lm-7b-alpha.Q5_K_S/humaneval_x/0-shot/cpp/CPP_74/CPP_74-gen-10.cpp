    int cnt1,cnt2,i;
    vector<string> ans;
    cnt1=lst1.size();
    cnt2=lst2.size();
    if(cnt1<cnt2)
    {
        ans=lst1;
    }
    else if(cnt1>cnt2)
    {
        ans=lst2;
    }
    else
    {
        for(i=0;i<cnt1;i++)
        {
            if(lst1[i].size()<lst2[i].size())
            {
                ans=lst1;
                break;
            }
            else if(lst1[i].size()>lst2[i].size())
            {
                ans=lst2;
                break;
            }
            else if(i==cnt1-1)
            {
                ans=lst1;
            }
        }
    }
    return ans;
}

int main(){
    vector<string> lst1={"hi","admin"},lst2={"hI","Hi"};
    vector<string> ans;
    ans=total_match(lst1,lst2);
    for(int i=0;i<ans.size();i++)
    {
        printf("%s ",ans[i]);
    }
    return 0;
}

































































































































































































