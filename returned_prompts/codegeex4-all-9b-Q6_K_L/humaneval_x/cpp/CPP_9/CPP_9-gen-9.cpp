#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> result;
    for(int i=0;i<numbers.size();i++){
        result.push_back(*max_element(numbers.begin(),numbers.begin()+i+1));
    }
    return result;
}

B:
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> result;
    for(int i=0;i<numbers.size();i++){
        result.push_back(*max_element(numbers.begin(),numbers.begin()+i));
    }
    return result;
}
C:
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> result;
    for(int i=0;i<numbers.size();i++){
        result.push_back(*max_element(numbers.begin(),numbers.begin()+i));
    }
    return result;
}
D:
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> result;
    for(int i=0;i<numbers.size();i++){
        result.push_back(max_element(numbers.begin(),numbers.begin()+i+1));
    }
    return result;
}
E:
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> result;
    for(int i=0;i<numbers.size();i++){
        result.push_back(max_element(numbers.begin(),numbers.begin()+i));
    }
    return result;
}
F:
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> result;
    for(int i=0;i<numbers.size();i++){
        result.push_back(*max_element(numbers.begin(),numbers.end()));
    }
    return result;
}
G:
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
    vector<int> result;
    for(int i=0;i<numbers.size();i++){
        result.push_back(*max_element(numbers.begin(),numbers.begin()+i+1));
    }
    return result;
}

H:
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
vector<int> rolling_max(vector<int> numbers){
   