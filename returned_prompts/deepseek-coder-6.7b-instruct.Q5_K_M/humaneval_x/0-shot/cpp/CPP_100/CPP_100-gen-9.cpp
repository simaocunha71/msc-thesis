    vector<int> stones;
    if(n%2==0){
        for(int i=0;i<n;i++){
            stones.push_back(n+2*i);
        }
    }
    else{
        for(int i=0;i<n;i++){
            stones.push_back(n+2*i);
        }
    }
    return stones;
}

int main(){
    int n;
    printf("Enter the number of levels: ");
    scanf("%d",&n);
    vector<int> result = make_a_pile(n);
    printf("Number of stones in each level: ");
    for(int i = 0;i<result.size();i++)
        printf("%d ",result[i]);
    printf("\n");
    return 0;
}

Output:
Enter the number of levels: 3
Number of stones in each level: 3 5 7 
*/
#include <stdio.h>
#include <vector>
using namespace std;

vector<int> make_a_pile(int n){
    vector<int> stones;
    int num = n;
    for(int i = 0; i < n; i++){
        stones.push_back(num);
        num += 2;
    }
    return stones;
}

int main(){
    int n;
    printf("Enter the number of levels: ");
    scanf("%d",&n);
    vector<int> result = make_a_pile(n);
    printf("Number of stones in each level: ");
    for(int i = 0; i < result.size(); i++)
        printf("%d ",result[i]);
    printf("\n");
    return 0;
}

Output:
Enter the number of levels: 3
Number of stones in each level: 3 5 7
*/

Both codes do the same thing. The first one uses the modulo operator to check if the number of levels is even or odd, and then calculates the number of stones in each level accordingly. The second one uses a loop to calculate the number of stones in each