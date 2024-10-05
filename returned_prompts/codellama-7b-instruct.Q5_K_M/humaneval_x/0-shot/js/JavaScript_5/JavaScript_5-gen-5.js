const intersperse = (numbers, delimeter) => numbers.length === 0 
                                            ? [] 
                                            : numbers.reduce((acc, val, i, arr) => {
                                                if (i < arr.length - 1) {
                                                    acc.push(val, delimeter);
                                                } else {
                                                    acc.push(val);
                                                }
                                                return acc;
                                            }, [])
