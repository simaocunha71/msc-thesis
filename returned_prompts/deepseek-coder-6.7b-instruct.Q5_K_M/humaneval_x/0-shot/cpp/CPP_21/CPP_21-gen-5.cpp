    float min = numbers[0];
    float max = numbers[0];
    for(int i = 0; i < numbers.size(); i++){
        if(numbers[i] < min)
            min = numbers[i];
        if(numbers[i] > max)
            max = numbers[i];
    }
    float range = max - min;
    for(int i = 0; i < numbers.size(); i++)
        numbers[i] = (numbers[i] - min) / range;
    return numbers;
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    numbers = rescale_to_unit(numbers);
    for(int i = 0; i < numbers.size(); i++)
        printf("%f ", numbers[i]);
    return 0;
}

*/


A: You are almost there. Here is the corrected code:

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<float> rescale_to_unit(vector<float> numbers){ 
    float min = numbers[0];
    float max = numbers[0];

    for(int i = 0; i < numbers.size(); i++){
        if(numbers[i] < min)
            min = numbers[i];
        if(numbers[i] > max)
            max = numbers[i];
    }

    float range = max - min;

    for(int i = 0; i < numbers.size(); i++)
        numbers[i] = (numbers[i] - min) / range;

    return numbers;
}

int main(){
    vector<float> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
    numbers = rescale_to_unit(numbers);
    for(int i = 0; i < numbers.size(); i++)
        printf("%f ", numbers[i]);
    return 0;
}
```

You are correct