    vector<int> pile;
    for(int i=0;i<n;i++){
        if(n%2==0){
            pile.push_back(n+2*i);
        }
        else{
            pile.push_back(n+2*i);
        }
    }
    return pile;
}

*/

int main(){
    int n;
    printf("Enter the number of levels:\n");
    scanf("%d",&n);
    vector<int> p = make_a_pile(n);
    printf("Number of stones in each level:\n");
    for(int i=0;i<p.size();i++){
        printf("%d ",p[i]);
    }
    printf("\n");
    return 0;
}

//C++/Practice/C++/make_a_pile/main.cpp
#include <iostream>
#include <vector>
#include "make_a_pile.h"

using namespace std;

int main()
{
    int n;
    cout << "Enter the number of levels: ";
    cin >> n;
    vector<int> p = make_a_pile(n);
    cout << "Number of stones in each level: ";
    for(int i=0; i<p.size(); i++)
    {
        cout << p[i] << " ";
    }
    cout << endl;
    return 0;
}

//C++/Practice/C++/make_a_pile/make_a_pile.cpp
#include "make_a_pile.h"

vector<int> make_a_pile(int n)
{
    vector<int> pile;
    for(int i=0; i<n; i++)
    {
        if(n%2 == 0)
        {
            pile.push_back(n + 2*i);
        }
        else
        {
            pile.push_back(n + 2*i);
        }
    }
    return pile;
}

//C++/