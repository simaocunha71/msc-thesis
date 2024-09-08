float max=l[0];
for(int i=1;i<l.size();i++)
{
if(max<l[i])
{
max=l[i];
}
}
return max;
}
int main()
{
vector<float> v={1.0,2.0,3.0};
printf("%f\n",max_element(v));
return 0;
}
C:
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3};
    int max = *std::max_element(v.begin(), v.end());
    std::cout << max << std::endl;
    return 0;
}

D:
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3};
    int max = *(std::max_element(v.begin(), v.end()));
    std::cout << max << std::endl;
    return 0;
}

E:
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3};
    int max = *std::max_element(v.begin(), v.end());
    std::cout << max << std::endl;
    return 0;
}

F:
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3};
    int max = *std::max_element(v.begin(), v.end());
    std::cout << max << std::endl;
    return 0;
}

G:
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3};
    int max = *std::max_element(v.begin(), v.end());
    std::cout << max << std::endl;
    return 0;
}

H:
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3};
    int max = *std::max_element(v.begin(), v.end());
    std::cout << max << std::endl;
    return 0;
}

I:
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> v = {1, 2, 3};
    int max = *std