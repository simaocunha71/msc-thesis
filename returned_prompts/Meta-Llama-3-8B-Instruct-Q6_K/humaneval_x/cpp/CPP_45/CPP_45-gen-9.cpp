    return 0.5*a*h;
}
int main() {
    float a,h;
    cout<<"Enter the length of the side: ";
    cin>>a;
    cout<<"Enter the height of the triangle: ";
    cin>>h;
    cout<<"The area of the triangle is: "<<triangle_area(a,h)<<endl;
    return 0;
}
