    vector<int> result;
    if(k>arr.size())
    {
        return result;
    }
    sort(arr.begin(),arr.end());
    for(int i=0;i<k;i++)
    {
        result.push_back(arr[arr.size()-1-i]);
    }
    return result;

}
int main(int argc, char const *argv[])
{
    vector<int> arr = {-3, -4, 5};
    vector<int> result=maximum(arr,3);
    for(int i=0;i<result.size();i++)
    {
        printf("%d ",result[i]);
    }
    return 0;
}
