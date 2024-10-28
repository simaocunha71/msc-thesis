
    vector<float> pos_list;
    for(int i=0; i<l.size(); i++){
        if(l[i]>0){
            pos_list.push_back(l[i]);
        }
    }
    return pos_list;
}


int main(){
    vector<float> l = {-1, 2, -4, 5, 6};
    vector<float> result = get_positive(l);
    for(int i=0; i<result.size(); i++){
        printf("%f ", result[i]);
    }
    return 0;
}

*/

#include <iostream>
#include <vector>
using namespace std;

vector<int> get_positive(vector<int> l)
{
    vector<int> positiveNumbers;
    for(int i=0; i<l.size(); i++)
    {
        if(l[i]>0)
        {
            positiveNumbers.push_back(l[i]);
        }
    }
    return positiveNumbers;
}

int main()
{
    vector<int> v = {-1, 2, -4, 5, 6};
    vector<int> result = get_positive(v);
    for(int i=0; i<result.size(); i++)
    {
        cout << result[i] << " ";
    }
    return 0;
}

*/

/*
