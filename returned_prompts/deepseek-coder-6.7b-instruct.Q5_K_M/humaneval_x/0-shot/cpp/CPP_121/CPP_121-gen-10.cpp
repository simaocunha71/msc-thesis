  int sum=0;
  for(int i=0;i<lst.size();i++){
    if(i%2==0 && lst[i]%2==1){
      sum+=lst[i];
    }
  }
  return sum;
}

int main(){
  vector<int> lst = {5, 8, 7, 1};
  printf("%d", solutions(lst));
  return 0;
}


A: You made a minor mistake while calling your function. You named it as 'solutions' but while calling in main function you used 'solutionss'. So, it should be 'solutions'.
Here is the corrected code:

```C++
#include<iostream>
#include<vector>
using namespace std;
int solutions(vector<int> lst){
  int sum=0;
  for(int i=0;i<lst.size();i++){
    if(i%2==0 && lst[i]%2==1){
      sum+=lst[i];
    }
  }
  return sum;
}
int main(){
  vector<int> lst = {5, 8, 7, 1};
  cout<<solutions(lst)<<endl;
  return 0;
}
```

Now, this code will give you the sum of all odd numbers in even position in your vector.


A: You can also use a range-based for loop to make your code cleaner and more readable. Here is the revised code:

```C++
#include<iostream>
#include<vector>
using namespace std;

int solution(vector<int> lst){
  int sum=0;
  for(int i=0;i<lst.size();i+=2){
    sum+=lst[i];
  }
  return sum;
}

int main(){
  vector<int> lst = {5, 8, 7, 1};
  cout<<solution(lst)<<endl;
  return 0;
}
```

In this code,