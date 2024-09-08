    vector<float> result;
    for(int i=0;i<l.size();i++){
        if(l[i]>0){
            result.push_back(l[i]);
        }
    }
    return result;
}

int main()
{
    vector<float> v = {-1, 2, -4, 5, 6};
    vector<float> result = get_positive(v);
    for(int i=0;i<result.size();i++){
        printf("%f ",result[i]);
    }
    return 0;
}

B:
    vector<float> get_positive(vector<float> l){
        return {v.begin(), find_if(v.begin(), v.end(), [](float x){ return x>0; });}
    }
    int main()
    {
        vector<float> v = {-1, 2, -4, 5, 6};
        vector<float> result = get_positive(v);
        for(int i=0;i<result.size();i++){
            printf("%f ",result[i]);
        }
        return 0;
    }
C:
    vector<float> get_positive(vector<float> l){
        vector<float> result;
        for(float x : l){
            if(x>0){
                result.push_back(x);
            }
        }
        return result;
    }
    int main()
    {
        vector<float> v = {-1, 2, -4, 5, 6};
        vector<float> result = get_positive(v);
        for(int i=0;i<result.size();i++){
            printf("%f ",result[i]);
        }
        return 0;
    }
D:
    vector<float> get_positive(vector<float> l){
        vector<float> result;
        for(int i=0;i<l.size();i++){
            if(l[i]>0){
                result.push_back(l[i]);
            }
        }
        return result;
    }
    int main()
    {
        vector<float> v = {-1, 2, -4, 5, 6};
        vector<float> result = get_positive(v);
        for(int i=0;i<result.size();i++){
            printf("%f ",result[i]);
        }
        return 0;
    }
E:
    vector<float> get_positive(vector<float> l){
        vector<float> result;
        for(float x : l){
            if(x>0){
                result.push_back(x);
            }
        }
        return result;
    }
    int main()
    {
        vector<float> v = {-1,