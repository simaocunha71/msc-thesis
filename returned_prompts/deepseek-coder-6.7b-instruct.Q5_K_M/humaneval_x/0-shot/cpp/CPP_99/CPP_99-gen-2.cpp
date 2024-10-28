    double num = stod(value);
    if(num >= 0){
        return (int)round(num);
    } else {
        return (int)round(num - 0.5) + 1;
    }
}

int main() {
    printf("%d\n", closest_integer("10"));
    printf("%d\n", closest_integer("15.3"));
    printf("%d\n", closest_integer("14.5"));
    printf("%d\n", closest_integer("-14.5"));
    return 0;
}

*/

