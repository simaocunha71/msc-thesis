    sort(l.begin(), l.end());
    for(int i = 0; i < l.size(); i++){
        int left = i + 1;
        int right = l.size() - 1;
        while(left < right){
            int sum = l[i] + l[left] + l[right];
            if(sum < 0){
                left++;
            }
            else if(sum > 0){
                right--;
            }
            else{
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<int> v1 = {1, 3, 5, 0};
    vector<int> v2 = {1, 3, -2, 1};
    vector<int> v3 = {1, 2, 3, 7};
    vector<int> v4 = {2, 4, -5, 3, 9, 7};
    vector<int> v5 = {1};
    printf("triples_sum_to_zero({%d, %d, %d, %d}) = %s\n", v1[0], v1[1], v1[2], v1[3], triples_sum_to_zero(v1)?"true":"false");
    printf("triples_sum_to_zero({%d, %d, %d, %d}) = %s\n", v2[0], v2[1], v2[2], v2[3], triples_sum_to_zero(v2)?"true":"false");
    printf("triples_sum_to_zero({%d, %d, %d, %d}) = %s\n", v3[0], v3[1], v3[2], v3[3], triples_sum_to_zero(v3)?"true":"false");
    printf("triples_sum_to_zero({%d, %d, %d, %d, %d, %d}) = %s\n", v4[0], v4[1], v4[2], v4[3], v4[4], v4[5], triples_sum_to_zero(v4)?"true":"false");
    printf("triples_sum_to_zero({%d}) = %s\n", v5[0], triples_sum_to_zero(v5)?"true":"false");
    return 0;
}  



C:
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

bool