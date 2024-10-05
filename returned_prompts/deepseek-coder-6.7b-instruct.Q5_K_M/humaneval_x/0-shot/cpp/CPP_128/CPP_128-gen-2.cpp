    if(arr.empty()){
        return -32768;
    }
    int product_sign = 1;
    int sum_magnitude = 0;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] < 0){
            product_sign *= -1;
        }
        else if(arr[i] > 0){
            product_sign *= 1;
        }
        else{
            return 0;
        }
        sum_magnitude += abs(arr[i]);
    }
    return product_sign * sum_magnitude;
}

int main()
{
    vector<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(2);
    arr.push_back(-4);
    printf("%d\n",prod_signs(arr)); // should return -9

    vector<int> arr1;
    arr1.push_back(0);
    arr1.push_back(1);
    printf("%d\n",prod_signs(arr1)); // should return 0

    vector<int> arr2;
    printf("%d\n",prod_signs(arr2)); // should return -32768

    return 0;
}
*/

#include <vector>
using namespace std;

int prod_signs(vector<int> arr){
    if(arr.empty()){
        return -32768;
    }

    int sum = 0, sign = 1;

    for(int num : arr){
        if(num < 0){
            sign *= -1;
            sum += abs(num);
        }
        else if(num > 0){
            sum += num;
        }
        else{
            return 0;
        }
    }

    return sign * sum;
}

int main(){
    vector<int> arr = {1, 2, 2, -4};
    printf("%d\n", prod_signs(arr)); // should return -9