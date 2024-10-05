Go
// The result can't be greater than p, so we can use % operator directly.
return (n%p+p)%p

Python
To avoid overflow, we use a while loop to calculate the result.
def Modp(n,p):
    r = 1
    while p != 0:
        if p & 1 == 1:
            r = (r * n) % p
        p = p >> 1
        n = (n * n) % p
    return r

JavaScript
To avoid overflow, we use a while loop to calculate the result.
function Modp(n,p){
    var r = 1;
    while (p > 0) {
        if (p % 2 == 1) {
            r = (r * n) % p;
        }
        n = (n * n) % p;
        p = Math.floor(p / 2);
    }
    return r;
}

Ruby
To avoid overflow, we use a while loop to calculate the result.
def Modp(n,p)
    r = 1
    while p != 0
        if (p % 2 == 1)
            r = (r * n) % p
        end
        n = (n * n) % p
        p >>= 1
    end
    return r
end

C++
To avoid overflow, we use a while loop to calculate the result.
#include <iostream>
using namespace std;

int Modp(int n,int p){
    int r = 1;
    while (p != 0){
        if (p & 1 == 1) r = (r * n) % p;
        n = (n * n) % p;
        p >>= 1;
    }
    return r;
}

C#
To avoid overflow, we use a while loop to calculate the result.
using System;
public class Modp
{
    public static int Modp(int n,int p){
        int r = 1;
        while (p != 0){
            if (p % 2 == 1) r = (r