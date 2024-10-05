    int count=0,n=grid.size(),m=grid[0].size();
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(grid[i][j]){
                count++;
            }
        }
    }
    return (count+capacity-1)/capacity;
*/

//main.c
#include <stdio.h>
#include "wells_and_buckets.c"

int main() {
    int