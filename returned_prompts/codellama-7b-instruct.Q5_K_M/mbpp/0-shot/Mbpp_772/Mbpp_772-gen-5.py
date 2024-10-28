```
import re


def remove_length(string, k):
    pattern = r'\w{{{}}}'.format(k)
    return re.sub(pattern, '', string)


assert remove_length('The person is most value tet', 3) == 'person is most value'
```
