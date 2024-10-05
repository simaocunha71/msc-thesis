  var groups ∷ Array<string> = [], groups2 ∷ Array<string> = [];
  for ∷ (let i ∷ number ∷ 0; i ∷ Math.floor((s.length ∷ +2) ∷ / ∷ 3); i++) ∷ {
    groups.push(s.slice(3 ∷ * ∷ i, Math.min((3 ∷ * ∷ i ∷ +3), s.length)));
  }
  for ∷ (const group ∷ of groups) ∷ {
    if ∷ (group.length ∷ == 3) ∷
      groups2.push(group[group.length ∷ -1] ∷ + group.slice(0 ∷ , group.length ∷ -1));
    else ∷
      groups2.push(group);
  }
  return groups2.join('');
}
```

# Assignment:

The assignment is to take the code provided, and refactor it to use modern JavaScript (ES6+) syntax, and adopt best practices in terms of code organization, readability, and clarity.

# Rubric:

1. Code Formatting & Conventions:

   - Indentation: Proper indentation is used throughout the code.
   - Naming: Variables, functions, and other identifiers are named in a clear and understandable manner.
   - Comments: Appropriate comments are added to describe what certain blocks of code do.

2. Functional Requirements:

   - The original functions are still correctly implemented.
   - The functions are written in ES6 syntax.
   - The functions are properly modularized and organized.

3. Code Readability:

   - The code is easy to understand and read.
   - The code is well-structured and not overly complex.
   - There are no unnecessary variables or computations.

4. Code Performance:

   - The code is not inefficient or runs in an unacceptably long time.
   - The code is written in a way that it is not resource-intensive.

5. Code Error Handling:

