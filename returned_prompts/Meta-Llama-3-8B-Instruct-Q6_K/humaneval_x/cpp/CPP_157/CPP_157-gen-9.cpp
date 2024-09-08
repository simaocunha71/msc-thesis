    if(a*a+b*b==c*c||a*a+c*c==b*b||b*b+c*c==a*a)
        return true;
    else
        return false;
}

int main()
{
    printf("%d\n",right_angle_triangle(3,4,5));
    printf("%d\n",right_angle_triangle(1,2,3));
    return 0;
}

Output:
1
0
Explanation:
The function right_angle_triangle() checks if the three given side lengths
form a right-angled triangle. It does this by checking if the sum of the squares of 
the two smaller sides is equal to the square of the largest side. If this condition 
is met, it returns true, indicating that the three sides form a right-angled 
triangle. Otherwise, it returns false.

The main() function tests the function with two sets of side lengths, (3, 4, 5) and 
(1, 2, 3), and prints the results. The first set of side lengths forms a right- 
angled triangle, so the output is 1. The second set of side lengths does not form 
a right-angled triangle, so the output is 0.