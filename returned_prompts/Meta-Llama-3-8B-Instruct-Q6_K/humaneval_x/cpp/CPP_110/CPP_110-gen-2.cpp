    // Check if lst1 contains any odd numbers
    for(int i = 0; i < lst1.size(); i++){
        if(lst1[i] % 2 != 0){
            // If lst1 contains an odd number, check if lst2 contains an even number
            for(int j = 0; j < lst2.size(); j++){
                if(lst2[j] % 2 == 0){
                    // If lst2 contains an even number, swap the elements and check again
                    swap(lst1[i], lst2[j]);
                    if(check(lst1, 0) == 1){
                        return "YES";
                    }
                    // If the function returns "YES", return "YES" from the main function
                    return "YES";
                }
            }
        }
    }
    return "NO";
}

// Function to check if lst1 contains only even numbers
int check(vector<int> lst, int pos){
    for(int i = pos; i < lst.size(); i++){
        if(lst[i] % 2 != 0){
            return 0;
        }
    }
    return 1;
}

int main() {
    vector<int> lst1 = {1, 2, 3, 4};
    vector<int> lst2 = {1, 5, 3, 4};
    printf("%s\n", exchange(lst1, lst2).c_str());
    return 0;
}
C:
// The C code is similar to the C++ code, the main difference is that
// the swap function is not available in C, so we have to implement it
#include<stdio.h>
#include<vector.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>

bool exchange(int *lst1, int *lst2, int n1, int n2){
    int i, j, temp;
    for(i = 0; i < n1; i++){
        if(lst1[i] % 2 != 0){
            for(j = 0; j < n2; j++){
                if(lst2[j] % 2 == 0){
                    temp = lst1[i];
                    lst1[i] = lst2[j];
                    lst2[j] = temp;
                    if(isOnlyEven(lst1, n1) == 1){
                        return 1;
                    }
                    temp = lst1[i];
                    lst1[i] = lst2[j];
                    lst2[j] = temp;
               