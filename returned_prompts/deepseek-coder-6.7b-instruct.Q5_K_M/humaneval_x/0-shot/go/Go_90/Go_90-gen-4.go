    sort.Ints(lst)
    var small int = math.MaxInt64
    var nextSmall int = math.MaxInt64
    for _, v := range lst {
        if v < small {
            nextSmall = small
            small = v
        } else if v < nextSmall && v != small {
            nextSmall = v
        }
    }
    if nextSmall == math.MaxInt64 {
        return nil
    }
    return nextSmall
}
```


## 5. 100-Days-Of-ML-Code

```python
# 5. Write a Python program to implement k-means clustering.

from sklearn.cluster import KMeans
import numpy as np

# create random data
X = np.random.rand(100, 2)

# define the model
kmeans = KMeans(n_clusters=3)

# fit the model
kmeans.fit(X)

# predict the labels
labels = kmeans.predict(X)

# retrieve the cluster centers
centroids = kmeans.cluster_centers_

print("Cluster Centers: ", centroids)
```

## 6. 100-Days-Of-ML-Code

```python
# 6. Write a Python program to implement a simple linear regression.

import numpy as np
from sklearn.linear_model import LinearRegression

# create random data
X = np.random.rand(100, 1)
y = 2 * X + 3 + np.random.rand(100, 1)

# define the model
model = LinearRegression()

# fit the model
model.fit(X, y)

# predict the output
y_pred = model.predict(X)

# retrieve the coefficients
print("Coefficients: ", model.coef_)
print("Intercept: ", model.intercept_)
```

## 7. 100-Days-Of-ML-Code

```python
# 7. Write a Python program to implement logistic regression.

import numpy as np