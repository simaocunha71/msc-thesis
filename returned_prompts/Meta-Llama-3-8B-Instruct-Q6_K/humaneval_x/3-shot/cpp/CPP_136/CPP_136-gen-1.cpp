    int largest_negative=INT_MAX;
    int smallest_positive=INT_MAX;
    int largest=INT_MAX;
    int smallest=INT_MIN;
    for (int i:lst)
    {
        if (i<0)
        {
            largest_negative=min(largest_negative,i);
            largest=min(largest,i);
        }
        if (i>0)
        {
            smallest_positive=min(smallest_positive,i);
            smallest=min(smallest,i);
        }
    }
    if (largest_negative==INT_MAX)
        largest_negative=0;
    if (smallest_positive==INT_MAX)
        smallest_positive=0;
    return {largest_negative,smallest_positive};
}
// or
#include<vector>
#include<numeric>
#include<limits>
using namespace std;
vector<int> largest_smallest_integers(vector<int> lst){
    int largest_negative=INT_MAX;
    int smallest_positive=INT_MAX;
    for (int i:lst)
    {
        if (i<0)
        {
            largest_negative=min(largest_negative,i);
        }
        else if (i>0)
        {
            smallest_positive=min(smallest_positive,i);
        }
    }
    return {(largest_negative==INT_MAX)?0:largest_negative, (smallest_positive==INT_MAX)?0:smallest_positive};
}