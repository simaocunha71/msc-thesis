    if (a <= 0 || b <= 0 || c <= 0) {
        return false;
    }
    if (a + b > c && b + c > a && c + a > b) {
        if (pow(a, 2) == (pow(b, 2) + pow(c, 2))) {
            return true;
        } else if (pow(b, 2) == (pow(a, 2) + pow(c, 2))) {
            return true;
        } else if (pow(c, 2) == (pow(b, 2) + pow(a, 2))) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}
int main()
{
    float a,b,c;
    scanf("%f%f%f",&a,&b,&c);
    if(right_angle_triangle(a,b,c))
    printf("true\n");
    else
    printf("false\n");
    return 0;
}



*/
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float a = sc.nextFloat(), b = sc.nextFloat(), c = sc.nextFloat();
        boolean right_angle_triangle = (a <= 0 || b <= 0 || c <= 0) ? false : true;
        if (a + b > c && b + c > a && c + a > b) {
            right_angle_triangle = (Math.pow(a, 2) == (Math.pow(b, 2) + Math.pow(c, 2))) ? true : (Math.pow(b, 2) == (Math.pow(a, 2) + Math.pow(c, 2))) ? true : (Math.pow(c, 2) == (Math.pow(b, 2) + Math.pow(a, 2))) ? true : false;
        } else {
            right_angle_triangle = false;
       