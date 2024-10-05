

def correct_bracketing(brackets: str):
    opening_brackets = "("<
    closing_brackets = ")>)"
    stack = []
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if len(stack) == 0:
                return False
            if stack[-1] == "(" and bracket == ")":
                stack.pop()
            else:
                return False
    return len(stack) == 0




# Made By Mostafa_Khaled
```
    
    
        
    
    
        
    
        
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    Welcome to Github! Thanks for contributing to open-source projects :)
    
    

To get started, check out our Contributing Guide.

Following these steps will help you and your fellow contributors create better software:

    
    
    - **Use a consistent coding style**: Pick one and stick to it! Most projects have a `.stylelintrc` file that specifies the rules. For example, PEP 8 is used by Python projects.
    - **Write tests**: Make sure your changes don't break existing functionality. If you're unsure whether a test is needed, err on the side of caution and add it. See the guide to writing tests for more information.
    - **Keep the change small**: It's easier to review and apply smaller, focused changes. If you're working on a large change, consider breaking it up into several smaller pull requests (PRs).
    - **Update documentation**: When you fix a bug or add a feature, make sure to update the documentation so that it's accurate and up-to-date.
    - **Review your changes**: Make sure your changes don't break anything, even if the build still passes. For example, check that your changes don't add lint errors or warnings. You can use GitHub Actions to check your pull request before it's merged.
    - **Squash commits**: When you're ready to merge your pull request, squash all your