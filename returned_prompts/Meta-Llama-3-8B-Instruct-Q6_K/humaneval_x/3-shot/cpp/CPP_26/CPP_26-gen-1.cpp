    vector<int> result;
    for (int i=0;i<numbers.size();i++)
    {
        if (find(result.begin(),result.end(),numbers[i]) == result.end())
        result.push_back(numbers[i]);
    }
    return result;
}
//or
#include<stdio.h>
#include<vector>
#include<set>
using namespace std;
vector<int> remove_duplicates(vector<int> numbers){
    set<int> s (numbers.begin(), numbers.end());
    vector<int> result (s.begin(), s.end());
    return result;
} 
//or
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> remove_duplicates(vector<int> numbers){
    vector<int> result;
    for (int i=0;i<numbers.size();i++)
    {
        if (find(result.begin(),result.end(),numbers[i]) == result.end())
        {
            result.push_back(numbers[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
} 
//or
#include<stdio.h>
#include<vector>
#include<unordered_map>
using namespace std;
vector<int> remove_duplicates(vector<int> numbers){
    unordered_map<int, int> m;
    vector<int> result;
    for (int i=0;i<numbers.size();i++)
    {
        if (m.find(numbers[i])==m.end())
        {
            m[numbers[i]]=1;
            result.push_back(numbers[i]);
        }
    }
    return result;
} 
//or
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> remove_duplicates(vector<int> numbers){
    vector<int> result;
    for (int i=0;i<numbers.size();i++)
    {
        bool found=false;
        for (int j=0;j<result.size();j++)
        {
            if (numbers[i]==result[j])
            {
                found=true;
                break;
            }
        }
        if (!found)
        {
            result.push_back(numbers[i]);
        }
    }
    return result;
} 
//or
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> remove_duplicates(vector<int> numbers){
    vector<int> result;
    for (int i=0;i<numbers.size();i++)
    {
        bool found=false;
        for (int j=0;j<result.size();j++)
        {
            if (numbers[i]==result[j])
            {
                found=true;
                break;
            }
        }
        if