    int sum = 0;
    int product = 1;
    for(int i=0; i<numbers.size(); i++){
        sum += numbers[i];
        product *= numbers[i];
    }
    return {sum, product};
}

int main(){
    vector<int> vec = {1, 2, 3, 4};
    vector<int> result = sum_product(vec);
    printf("(%d, %d)\n", result[0], result[1]);
    return 0;
}

*/

#include <stdio.h>

int main(){
    int numbers[] = {1, 2, 3, 4};
    int sum = 0;
    int product = 1;
    for(int i=0; i<4; i++){
        sum += numbers[i];
        product *= numbers[i];
    }
    printf("(%d, %d)\n", sum, product);
    return 0;
}

/*

