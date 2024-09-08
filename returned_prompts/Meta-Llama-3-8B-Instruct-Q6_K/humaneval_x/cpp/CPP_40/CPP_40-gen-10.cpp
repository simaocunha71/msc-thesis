    if(l.size()<3)
    {
        return false;
    }
    for(int i=0;i<l.size();i++)
    {
        for(int j=i+1;j<l.size();j++)
        {
            for(int k=j+1;k<l.size();k++)
            {
                if(l[i]+l[j]+l[k]==0)
                {
                    return true;
                }
            }
        }
    }
    return false;
}

int main()
{
    vector<int> l1={1,3,5,0};
    vector<int> l2={1,3,-2,1};
    vector<int> l3={1,2,3,7};
    vector<int> l4={2,4,-5,3,9,7};
    vector<int> l5={1};
    printf("%d\n",triples_sum_to_zero(l1)); //false
    printf("%d\n",triples_sum_to_zero(l2)); //true
    printf("%d\n",triples_sum_to_zero(l3)); //false
    printf("%d\n",triples_sum_to_zero(l4)); //true
    printf("%d\n",triples_sum_to_zero(l5)); //false
    return 0;
}

B:
    bool triples_sum_to_zero(vector<int> l) {
        sort(l.begin(), l.end());
        for (int i = 0; i < l.size() - 2; i++) {
            int left = i + 1;
            int right = l.size() - 1;
            while (left < right) {
                int sum = l[i] + l[left] + l[right];
                if (sum < 0) {
                    left++;
                } else if (sum > 0) {
                    right--;
                } else {
                    return true;
                }
            }
        }
        return false;
    }
C:
    bool triples_sum_to_zero(vector<int> l) {
        unordered_map<int, int> count;
        for (int num : l) {
            if (count.find(-num) != count.end()) {
                return true;
            }
            count[num]++;
        }
        return false;
    }
D:
    bool triples_sum_to_zero(vector<int> l) {
        sort(l.begin(), l.end());
        for (int i = 0; i < l.size() - 2; i++) {
            int left = i + 1;
            int right = l.size