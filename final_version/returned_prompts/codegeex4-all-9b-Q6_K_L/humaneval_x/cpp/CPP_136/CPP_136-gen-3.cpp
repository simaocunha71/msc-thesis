#include <vector>
#include <algorithm>

using namespace std;

vector<int> largest_smallest_integers(vector<int> lst){
    vector<int> result(2, 0);
    if(lst.size() == 0)
        return result;

    int largest_negative = 0;
    int smallest_positive = 0;

    for(int i = 0; i < lst.size(); i++){
        if(lst[i] < 0 && lst[i] < largest_negative)
            largest_negative = lst[i];
        else if(lst[i] > 0 && lst[i] < smallest_positive)
            smallest_positive = lst[i];
    }

    result[0] = largest_negative;
    result[1] = smallest_positive;
    return result;
}

B:
#include <vector>
#include <algorithm>

using namespace std;

vector<int> largest_smallest_integers(vector<int> lst){
    if(lst.empty())
        return {0, 0};
    int largest_negative = *min_element(lst.begin(), lst.end());
    int smallest_positive = *max_element(lst.begin(), lst.end());

    if(largest_negative < 0)
        return {largest_negative, smallest_positive};
    else
        return {0, smallest_positive};
}

C:
#include <vector>
#include <algorithm>

using namespace std;

vector<int> largest_smallest_integers(vector<int> lst){
    if(lst.empty())
        return {0, 0};
    int largest_negative = *min_element(lst.begin(), lst.end());
    int smallest_positive = *max_element(lst.begin(), lst.end());

    if(largest_negative >= 0)
        return {0, smallest_positive};
    else
        return {largest_negative, smallest_positive};
}

D:
#include <vector>
#include <algorithm>

using namespace std;

vector<int> largest_smallest_integers(vector<int> lst){
    if(lst.empty())
        return {0, 0};
    int largest_negative = *min_element(lst.begin(), lst.end());
    int smallest_positive = *max_element(lst.begin(), lst.end());

    if(largest_negative < 0)
        return {largest_negative, smallest_positive};
    else
        return {0, smallest_positive};
}

E:
#include <vector>
#include <algorithm>

using namespace std;

vector<int> largest_smallest_integers(vector<int> lst){
    if(lst.empty())
        return {0, 0};
    int largest_negative = *min_element(lst.begin(), lst.end());
    int smallest_positive = *max_element(lst