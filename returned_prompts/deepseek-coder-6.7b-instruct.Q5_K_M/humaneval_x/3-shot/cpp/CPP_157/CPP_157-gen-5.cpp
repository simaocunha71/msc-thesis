    float max_side=max(a,max(b,c));
    float other_two=a+b+c-max_side;
    return (max_side*max_side)==(other_two*other_two)+(other_two*other_two);
}


