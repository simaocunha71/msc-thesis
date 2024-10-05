    int freq[5000];
    for(int i=0;i<5000;i++) freq[i]=0;
    for(int i=0;i<lst.size();i++) freq[lst[i]]++;
    for(int i=lst.size();i>0;i--) if(freq[i]>=i) return i;
    return -1;
}

int main(){
    vector<int> a={4,1,2,2,3,1};
    vector<int> b={1,2,2,3,3,3,4,4,4};
    vector<int> c={5,5,4,4,4};
    printf("%d\n",search(a));
    printf("%d\n",search(b));
    printf("%d\n",search(c));
    return 0;
}
*/

#include <vector>
using namespace std;
int search(vector<int> lst){
    int freq[5000];
    for(int i=0;i<5000;i++) freq[i]=0;
    for(int i=0;i<lst.size();i++) freq[lst[i]]++;
    for(int i=lst.size();i>0;i--) if(freq[i]>=i) return i;
    return -1;
}

//test/001_search_greatest_freq_greater_than_itself/001_search_greatest_freq_greater_than_itself.t.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "001_search_greatest_freq_greater_than_itself.cpp"

TEST_CASE("Testing search function"){
    vector<int> a={4,1,2,2,3,1};
    vector<int> b={1,2