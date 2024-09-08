/*
xs represent coefficients of a polynomial.
xs{0} + xs{1} * x + xs{2} * x^2 + ....
 Return derivative of this polynomial in the same form.
>>> derivative({3, 1, 2, 4, 5})
{1, 4, 12, 20}
>>> derivative({1, 2, 3})
{2, 6}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> derivative(vector<float> xs){
    int i;
    for(i=xs.size()-1;i>0;i--){
        xs[i]=xs[i-1]*i;
        xs.pop_back();
    }
    return xs;
}

B:
/*
xs represent coefficients of a polynomial.
xs{0} + xs{1} * x + xs{2} * x^2 + ....
 Return derivative of this polynomial in the same form.
>>> derivative({3, 1, 2, 4, 5})
{1, 4, 12, 20}
>>> derivative({1, 2, 3})
{2, 6}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> derivative(vector<float> xs){
    int i;
    for(i=xs.size()-1;i>0;i--){
        xs[i]=xs[i-1]*i;
    }
    xs.pop_back();
    return xs;
}

C:
/*
xs represent coefficients of a polynomial.
xs{0} + xs{1} * x + xs{2} * x^2 + ....
 Return derivative of this polynomial in the same form.
>>> derivative({3, 1, 2, 4, 5})
{1, 4, 12, 20}
>>> derivative({1, 2, 3})
{2, 6}
*/
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
vector<float> derivative(vector<float> xs){
    int i;
    for(i=xs.size()-1;i>0;i--){
        xs[i]=xs[i-1]*i;
        xs.erase(xs.begin()+i-1);
    }
    return xs;
}

D:
/*
xs represent coefficients of a polynomial.
xs{0} + xs{1} * x + xs{2} * x^2 + ....
 Return derivative of this polynomial in the same form.
>>>