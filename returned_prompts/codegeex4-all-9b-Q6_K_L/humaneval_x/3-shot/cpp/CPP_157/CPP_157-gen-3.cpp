    float max_side;
    if (a>b && a>c) max_side=a;
    else if (b>a && b>c) max_side=b;
    else max_side=c;
    float sum_of_other_sides;
    if (a==max_side) {sum_of_other_sides=b+c;return (sum_of_other_sides==pow(max_side,2));}
    if (b==max_side) {sum_of_other_sides=a+c;return (sum_of_other_sides==pow(max_side,2));}
    if (c==max_side) {sum_of_other_sides=a+b;return (sum_of_other_sides==pow(max_side,2));}
    
}

