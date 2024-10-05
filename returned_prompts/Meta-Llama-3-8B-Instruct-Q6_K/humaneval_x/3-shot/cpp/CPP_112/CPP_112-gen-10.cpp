    string result=s;
    for (char chr:c)
    {
        result.erase(remove(result.begin(),result.end(),chr),result.end());
    }
    string rev=result;
    reverse(rev.begin(),rev.end());
    if (result==rev)
        return {result,"True"};
    else
        return {result,"False"};
}