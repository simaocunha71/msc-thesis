    float temp;

    //Sort the sides in ascending order
    if(a > b){
        temp = a;
        a = b;
        b = temp;
    }
    if(b > c){
        temp = b;
        b = c;
        c = temp;
    }
    if(a > b){
        temp = a;
        a = b;
        b = temp;
    }

    //Check if the triangle is right-angled
    if(pow(c, 2) == pow(a, 2) + pow(b, 2))
        return true;
    else
        return false;
}

int main(){
    int x, y, z;
    scanf("%d %d %d", &x, &y, &z);
    if(right_angle_triangle(x, y, z))
        printf("true");
    else
        printf("false");
    return 0;
}
*/


A: This code first sorts the lengths of the sides a, b, and c in ascending order. Then, it checks if the square of the longest side c is equal to the sum of the