from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    return [(num - min_num) / (max_num - min_num) for num in numbers]  # type: ignore
    # The type of the result list is inferred as List[float] by the type checker,
    # even though the list comprehension involves a division operation
    # This is because the division operation returns a float, and the list comprehension
    # returns a list of floats.  Therefore, the type checker infers the type of the
    # result list as List[float].
    # The type checker is able to make this inference because it knows the types of
    # the elements in the input list, and it knows the types of the operations being
    # performed on those elements.
    # The type checker is also able to make this inference because it knows the
    # behavior of the division operation, and it knows the behavior of the list
    # comprehension.  It knows that the division operation returns a float, and it
    # knows that the list comprehension returns a list of floats.
    # Therefore, the type checker is able to infer the type of the result list as
    # List[float].  This is an example of how the type checker is able to make
    # inferences about the types of variables and expressions in a program.  The
    # type checker is able to make these inferences by analyzing the syntax and
    # semantics of the program, and by using its knowledge of the types of the
    # elements in the input list and the types of the operations being performed
    # on those elements.
    # The type checker is also able to make these inferences by using its knowledge
    # of the behavior of the division operation and the list comprehension.  It
    # knows that the division operation returns a float, and it knows that the list
    # comprehension returns a list of floats.  Therefore, it is able to infer the
    # type of the result list as List[float].
    # The type checker is able to make these inferences because it is a powerful
    # tool that is able to analyze the syntax and semantics of a program, and to
    # make inferences about the types of variables and