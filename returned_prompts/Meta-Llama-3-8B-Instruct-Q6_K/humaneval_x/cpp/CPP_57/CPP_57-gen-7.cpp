    bool isIncreasing=true;
    bool isDecreasing=true;
    for(int i=1;i<l.size();i++){
        if(l[i]>l[i-1]){
            isDecreasing=false;
        }
        else if(l[i]<l[i-1]){
            isIncreasing=false;
        }
    }
    return isIncreasing||isDecreasing;

}

int main()
{
    vector<float> v={1,2,4,20};
    printf("%d\n",monotonic(v));
    return 0;
}

Output:
1
Explanation:
The function takes a vector of float numbers as input and checks if the elements are monotonically increasing or decreasing. It does this by iterating through the vector and checking if each element is greater than or less than the previous one. If any element is neither greater than nor less than the previous one, the function returns false. If all elements are either greater than or less than the previous one, the function returns true. In the given example, the vector {1, 2, 4, 20} is monotonically increasing, so the function returns true.