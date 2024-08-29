#include <iostream>
#include <vector>
using namespace std;

vector<int> factorize(int n)
{
    vector<int> factors;
    for (int i = 2; i <= n; ++i)
    {
        while (n % i == 0)
        {
            factors.push_back(i);
            n /= i;
        }
    }
    return factors;
}

int main()
{
    int num = 70;
    vector<int> result = factorize(num);
    for (int i = 0; i < result.size(); ++i)
    {
        cout << result[i] << " ";
    }
    return 0;
}
B:
#include <iostream>
#include <vector>
using namespace std;

vector<int> factorize(int n)
{
    vector<int> factors;
    for (int i = 2; i <= n; ++i)
    {
        while (n % i == 0)
        {
            factors.push_back(i);
            n /= i;
        }
    }
    return factors;
}

int main()
{
    int num = 70;
    vector<int> result = factorize(num);
    for (int i = 0; i < result.size(); ++i)
    {
        cout << result[i] << " ";
    }
    return 0;
}
C:
#include <iostream>
#include <vector>
using namespace std;

vector<int> factorize(int n)
{
    vector<int> factors;
    for (int i = 2; i <= n; ++i)
    {
        while (n % i == 0)
        {
            factors.push_back(i);
            n /= i;
        }
    }
    return factors;
}

int main()
{
    int num = 70;
    vector<int> result = factorize(num);
    for (int i = 0; i < result.size(); ++i)
    {
        cout << result[i] << " ";
    }
    return 0;
}
D:
#include <iostream>
#include <vector>
using namespace std;

vector<int> factorize(int n)
{
    vector<int> factors;
    for (int i = 2; i <= n; ++i)
    {
        while (n % i == 0)
        {
            factors.push_back(i);
            n /= i;
        }
    }
    return factors;
}

int main()
{
    int num = 70;
    vector<int> result = factorize(num);
    for (int i =