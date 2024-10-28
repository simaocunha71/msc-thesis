
import hashlib


def string_to_md5(text):
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest() if text else None


# Alternatively, you can use the built-in hashlib library:
# from hashlib import md5
# def string_to_md5(text):
#     md5_hash = md5()
#     md5_hash.update(text.encode('utf-8'))
#     return md5_hash.hexdigest() if text else None


# Then you can test your function using doctest:
from doctest import TEST_MATURE, Output, FileFixture
from doctest import DocTestParser

class MyDocTestParser(DocTestParser):
    def get_test_from_file(self, filename, test_source, test_options):
        with open(filename) as f:
            return self.get_test_from_text(f.read(), test_source, test_options)

parser = MyDocTestParser(TEST_MATURE)
result = parser.parse(globals()['__file__'], pythonpath=['.'], doctest_modules=['__main__'])
if result.failed:
    exit(result.test.longmsg)


```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

``