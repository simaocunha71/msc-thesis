```c
#include<vector>
#include<algorithm>
using namespace std;
float max_element(vector<float> l){
    return *max_element(l.begin(), l.end());
}
```

B:
```c
#include<vector>
#include<algorithm>
using namespace std;
float max_element(vector<float> l){
    float max = l[0];
    for(int i=1;i<l.size();i++)
        if(l[i]>max)
            max = l[i];
    return max;
}
```

C:
```c
#include<vector>
#include<algorithm>
using namespace std;
float max_element(vector<float> l){
    float max = l[0];
    for(int i=1;i<l.size();i++)
        max = fmaxf(l[i], max);
    return max;
}
```

D:
```c
#include<vector>
#include<algorithm>
using namespace std;
float max_element(vector<float> l){
    float max = l[0];
    for(int i=1;i<l.size();i++)
        max = fmax(l[i], max);
    return max;
}
```

E:
```c
#include<vector>
#include<algorithm>
using namespace std;
float max_element(vector<float> l){
    float max = l[0];
    for(int i=1;i<l.size();i++)
        max = max(l[i], max);
    return max;
}
```

F:
```c
#include<vector>
#include<algorithm>
using namespace std;
float max_element(vector<float> l){
    float max = l[0];
    for(int i=1;i<l.size();i++)
        max = fmaxf(l[i], max);
    return max;
}
```

G:
```c
#include<vector>
#include<algorithm>
using namespace std;
float max_element(vector<float> l){
    float max = l[0];
    for(int i=1;i<l.size();i++)
        max = fmax(l[i], max);
    return max;
}
```

H:
```c
#include<vector>
#include<algorithm>
using namespace std;
float max_element(vector<float> l){
    float max = l[0];
    for(int i=1;i<l.size();i++)
        max = maxf(l[i], max);
    return max;
}
```



