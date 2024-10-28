    vector<int> ans(n, 0);
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            int res = 1;
            for (int j = 2; j <= i; j++) {
                res *= j;
            }
            ans[i] = res;
        } else {
            int res = 0;
            for (int j = 1; j <= i; j++) {
                res += j;
            }
            ans[i] = res;
        }
    }
    return ans;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> ans = f(n);
    for (int i = 0; i < n; i++) {
        printf("%d ", ans[i]);
    }
    return 0;
}



/*
What's the runtime of this program?
What is the space complexity of this program?
Is this program efficient? Why or why not?
What's the Big O of this program?

Answer:
The runtime of this program is O(n).
The space complexity of this program is O(n).
This program is not efficient because it calculates all factorial values that are not needed for the result.
The Big O of this program is O(n).

Explanation:
In this program, we calculate all factorial values that are not needed for the result. For example, if we are asked to calculate the sum from 1 to 5, we don't need to know the factorial of 3 and 5. However, the program calculates all factorial values from 1 to n, which increases the runtime and space complexity of the program.

To make the program more efficient, we can modify it to calculate the factorial values only when necessary. For example, if we are asked to calculate the sum from 1 to 5, we can directly calculate the result without calculating the factorial values. Similarly, if we are asked to calculate the factorial of an even number, we can directly calculate the result without calculating the sum values.

By modifying the program to calculate the factorial values only