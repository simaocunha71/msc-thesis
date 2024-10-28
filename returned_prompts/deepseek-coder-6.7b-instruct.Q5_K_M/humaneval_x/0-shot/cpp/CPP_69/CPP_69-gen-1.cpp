    int n = lst.size();
    int freq[n+1] = {0};

    for (int i=0; i<n; i++)
        freq[lst[i]]++;

    for (int i=n; i>=1; i--){
        if (freq[i]>=i)
            return i;
    }
    return -1;
}

int main(){
    vector<int> vec1 = {4, 1, 2, 2, 3, 1};
    vector<int> vec2 = {1, 2, 2, 3, 3, 3, 4, 4, 4};
    vector<int> vec3 = {5, 5, 4, 4, 4};
    printf("%d\n", search(vec1));
    printf("%d\n", search(vec2));
    printf("%d\n", search(vec3));
    return 0;
}
*/

#include<stdio.h>
#include<vector>
using namespace std;
int search(vector<int> lst){
    int n = lst.size();
    int freq[n+1] = {0};
    for (int i=0; i<n; i++)
        freq[lst[i]]++;
    for (int i=n; i>=1; i--){
        if (freq[i]>=i)
            return i;
    }
    return -1;
}

int main(){
    vector<int> vec1 = {4, 1, 2, 2, 3, 1};
    vector<int> vec2 = {1, 2, 2, 3, 3, 3, 4, 4, 4};
    vector<int> vec3 = {5, 5, 4, 4, 4};
    printf("%d\n", search(vec1));
    printf("%d\n", search(vec2));
    printf("%d\n", search(vec3));
    return 0;
}
