
The first problem I noticed is that you are not including the necessary headers in your program. In your first code block, you should have included <algorithm> as well:
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <math.h>
using namespace std;

The second problem is that you are using a for loop that does not start from 0. The for loop in the function has_close_elements() starts from 1 and goes to numbers.size(). This means that the first element of the vector is never checked. You should change the loop to start from 0:
for (i = 0; i < numbers.size(); i++)

The third problem is that you are using a for loop that does not start from 0. The for loop in the function separate_paren_groups() starts from 0 and goes to paren_string.length(). This means that the last element of the vector is never checked. You should change the loop to start from 0:
for (i = 0; i < paren_string.length(); i++)

The fourth problem is that you are using a for loop that does not start from 0. The for loop in the function specialFilter() starts from 0 and goes to nums.size(). This means that the first element of the vector is never checked. You should change the loop to start from 0:
for (i = 0; i < nums.size(); i++)

The fifth problem is that you are using a for loop that does not start from 0. The for loop in the function truncate_number() starts from 0 and goes to number. This means that the last element of the vector is never checked. You should change the loop to start from 0:
for (i = 0; i < number; i++)