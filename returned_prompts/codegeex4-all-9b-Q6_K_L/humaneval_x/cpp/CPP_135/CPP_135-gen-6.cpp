int size = arr.size();
  if(size == 0)
    return -1;
  int max_index = 0;
  for(int i = 1; i < size; i++){
    if(arr[i] < arr[i - 1]){
      max_index = i - 1;
      break;
    }
  }
  return max_index;
}

int main(){
  vector<int> arr = {1,2,4,3,5};
  printf("%d\n", can_arrange(arr));  // Outputs: 2
  arr = {1,2,3};
  printf("%d\n", can_arrange(arr));  // Outputs: -1
  return 0;
} 

B:
#include<stdio.h>
#include<vector>
using namespace std;
int can_arrange(vector<int> arr){

int size = arr.size();
  if(size == 0)
    return -1;
  int max_index = 0;
  for(int i = 1; i < size; i++){
    if(arr[i] < arr[i - 1]){
      max_index = i - 1;
      break;
    }
  }
  return max_index;
}

int main(){
  vector<int> arr = {1,2,4,3,5};
  printf("%d\n", can_arrange(arr));  // Outputs: 2
  arr = {1,2,3};
  printf("%d\n", can_arrange(arr));  // Outputs: -1
  return 0;
} 

C:
#include<stdio.h>
#include<vector>
using namespace std;
int can_arrange(vector<int> arr){

int size = arr.size();
  if(size == 0)
    return -1;
  int max_index = 0;
  for(int i = 1; i < size; i++){
    if(arr[i] < arr[i - 1]){
      max_index = i - 1;
      break;
    }
  }
  return max_index;
}

int main(){
  vector<int> arr = {1,2,4,3,5};
  printf("%d\n", can_arrange(arr));  // Outputs: 2
  arr = {1,2,3};
  printf("%d\n", can_arrange(arr));  // Outputs: -1
  return 0;
} 

D:
#include<stdio.h>
#include<vector>
using namespace std;
int can_arrange(vector<int> arr){

int size = arr.size