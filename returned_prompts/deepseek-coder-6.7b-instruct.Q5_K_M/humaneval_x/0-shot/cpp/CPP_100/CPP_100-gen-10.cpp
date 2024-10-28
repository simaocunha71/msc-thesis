    vector<int> res;
    for(int i=0;i<n;i++){
        if(n%2==0){
            res.push_back(n+2*i);
        }else{
            res.push_back(n+2*i);
        }
    }
    return res;
}

int main(){
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    vector<int> res = make_a_pile(n);
    for(int i=0;i<n;i++){
        printf("%d ",res[i]);
    }
    printf("\n");
    return 0;
}

Note:
This code is written in C++.
*/

/*

Test Cases:

Test Case 1:
    Input: 3
    Output: {3, 5, 7}

Test Case 2:
    Input: 4
    Output: {4, 6, 8, 10}

Test Case 3:
    Input: 5
    Output: {5, 7, 9, 11, 13}

Test Case 4:
    Input: 6
    Output: {6, 8, 10, 12, 14, 16}

Test Case 5:
    Input: 7
    Output: {7, 9, 11, 13, 15, 17, 19}

Test Case 6:
    Input: 8
    Output: {8, 10, 12, 14, 16, 18, 20, 22}
*/

// Code Ends here

// Do not edit the code below this line
// -----------------------------

// Code Ends here


// Code Ends here

// Do not edit the code below this line
// -----------------------------

// Code Ends here


// Code Ends here

// Do not edit the code below this line
// -----------------------------

// Code Ends here


// Code