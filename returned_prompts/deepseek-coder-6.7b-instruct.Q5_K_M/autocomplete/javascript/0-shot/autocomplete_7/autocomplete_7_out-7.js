
  var ret = '';
  for (var i = 0; i < n; ++i) {
    ret += list.shift();
  }
  return ret;
}

// Returns a string representing the current state of the state machine.
function getState() {
  return 'state: ' + this.state + ', buffer: ' + this.buffer.length;
}

// Resets the state machine to its initial state.
function reset() {
  this.state = this.initialState;
  this.buffer = [];
}

// Constructor for the state machine.
function StateMachine() {
  this.state = 'initial';
  this.buffer = [];
}

StateMachine.prototype = {
  consume: consume,
  copyFromBuffer: copyFromBuffer,
  getState: getState,
  reset: reset
};

// Export the StateMachine constructor for use in other modules.
module.exports = StateMachine;
```

## 8.10

```javascript
// Defines a class that represents a point in 2D space.
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  // Returns the distance between this point and another point.
  distanceTo(other) {
    const dx = this.x - other.x;
    const dy = this.y - other.y;
    return Math.sqrt(dx * dx + dy * dy);
  }

  // Returns a string representation of this point.
  toString() {
    return `(${this.x}, ${this.y})`;
  }
}
```

## 8.11

```javascript
// Returns a new array with all elements that pass the test implemented by the provided function.
function filter(array, testFunction) {
  let filteredArray = [];
  for (let i = 0; i < array.length; i++) {
    if (testFunction(array[i])) {
      filteredArray.push(array[i]);
    }
  }
  return filteredArray;
}

// Returns a new array with the results of calling a provided function