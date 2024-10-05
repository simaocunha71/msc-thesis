    vector<int> arr;
    int i,j,k;
    if(n==0)
    {
        return arr;
    }
    for(i=2;i<=n;i++)
    {
        int flag=0;
        for(j=2;j<i;j++)
        {
            if(i%j==0)
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
        {
            arr.push_back(i);
        }
    }
    return arr;
}

int main()
{
    int n;
    scanf("%d",&n);
    vector<int> arr;
    arr=count_up_to(n);
    for(int i=0;i<arr.size();i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    return 0;
}







*/
#include <bits/stdc++.h>
using namespace std;

vector<int> primes;

void sieve(int n) {
	primes.push_back(2);
	for (int i = 3; i <= n; i += 2) {
		if (isPrime(i)) {
			primes.push_back(i);
		}
	}
}

bool isPrime(int n) {
	if (n <= 1) {
		return false;
	}
	if (n <= 3) {
		return true;
	}
	if (n % 2 == 0 || n % 3 == 0) {
		return false;
	}
	for (int i = 5; i * i <= n; i += 6) {
		if (n % i == 0 || n % (i + 2) == 0) {
			return false;
		}
	}
	return true;
}

vector<int> count_up_to(int n) {
	sieve(n);
	