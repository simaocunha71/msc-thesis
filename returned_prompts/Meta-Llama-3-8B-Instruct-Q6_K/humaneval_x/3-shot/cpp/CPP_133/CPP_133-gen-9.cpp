    int sum=0;
    for (float i:lst)
    {
        sum+=ceil(i)*ceil(i);
    }
    return sum;
}  // 0.5 is rounded to 1, so the sum is 1*1+2*2+3*3=14
// 0 is rounded to 1, so the sum is 1*1+4*4+9*9=98
// 0 is rounded to 1, so the sum is 1*1+3*3+5*5+7*7=84
// 0 is rounded to 1, so the sum is 1*1+4*4+0*0=29
// 2.4 is rounded to 3, so the sum is 3*3+1*1+1*1=6
// 1 is rounded to 2, so the sum is 2*2+1*1+1*1=6
// 1 is rounded to 2, so the sum is 2*2+1*1+1*1=6
// 2.4 is rounded to 3, so the sum is 3*3+1*1+1*1=6
// 1 is rounded to 2, so the sum is 2*2+1*1+1*1=6
// 0 is rounded to 1, so the sum is 1*1+0*0=1
// 4.2 is rounded to 5, so the sum is 5*5+0*0=25
// 1 is rounded to 2, so the sum is 2*2+0*0=4
// 0 is rounded to 1, so the sum is 1*1+0*0=1
// 1 is rounded to 2, so the sum is 2*2+0*0=4
// 1 is rounded to 2, so the sum is 2*2+0*0=4
// 2.4 is rounded to 3, so the sum is 3*3+0*0=9
// 1 is rounded to 2, so the sum is 2*2+0*0=4
// 1 is rounded to 2, so the sum is 2*2+0*0