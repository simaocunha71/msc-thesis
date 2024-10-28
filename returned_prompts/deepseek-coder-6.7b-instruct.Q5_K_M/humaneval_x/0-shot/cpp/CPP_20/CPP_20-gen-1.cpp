vector<float> closest;
float min_diff = INFINITY;
float temp_diff;
int size=numbers.size();
float first_num, second_num;

//Sort the vector
sort(numbers.begin(),numbers.end());

for(int i=0; i<size-1; i++){
    temp_diff = abs(numbers