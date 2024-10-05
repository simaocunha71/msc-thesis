    string result="";
    for(int i=0;i<s.length();i++)
    {
        bool found=false;
        for(int j=0;j<c.length();j++)
        {
            if(s[i]==c[j])
            {
                found=true;
                break;
            }
        }
        if(!found)
            result+=s[i];
    }
    string rev_result=result;
    reverse(rev_result.begin(),rev_result.end());
    vector<string> res;
    res.push_back(rev_result);
    res.push_back((result==rev_result)?"True":"False");
    return res;
}  // 1.5 / 2
// 0.5 / 2
// 1 / 2
// 1 / 2
// 1 / 1
// 1 / 1
// 1 / 1
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 1
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 0.5 / 1
// 1 / 2
// 0.5 / 1
// 