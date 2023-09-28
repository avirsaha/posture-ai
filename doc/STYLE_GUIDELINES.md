
# Project Style Guidelines

This document outlines the coding style and conventions to be followed in our Python project. These guidelines are designed to ensure code consistency, readability, and maintainability across the project.

## 1. PEP 8 Compliance

We adhere to the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) for Python code. Please follow these key PEP 8 principles:

- Use 4 spaces per indentation level.
- Limit lines to 79 characters for code and 72 for docstrings and comments.
- Use clear and descriptive variable and function names.
- Use whitespace to improve code readability.

```python
# Good
def calculate_average(numbers: List[float]) -> float:
    total = sum(numbers)
    count = len(numbers)
    return total / count

# Bad
def avg(nums: List[float]) -> float:
    t = sum(nums)
    c = len(nums)
    return t / c
```

## 2. Type Annotations

We heavily rely on type annotations to enhance code clarity and catch type-related errors early. Ensure that all function parameters and return values are properly annotated. Use type hints from the `typing` module when necessary.

```python
from typing import List

def process_data(data: List[str]) -> List[str]:
    """Processes a list of strings and returns a list of processed strings."""
    result = [process_string(item) for item in data]
    return result
```

## 3. Functional Paradigm

We prefer a functional programming style where feasible. Write pure functions that do not have side effects and avoid mutating data in-place.

```python
from typing import List

def square_all(numbers: List[int]) -> List[int]:
    """Return a new list containing the squares of all numbers in the input list."""
    return [x ** 2 for x in numbers]
```

## 4. Documentation

Document your code thoroughly. Use clear and concise docstrings to explain the purpose of functions, classes, and modules. Include examples where appropriate.

```python
def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of `a` and `b`.

    Example:
        >>> add(2, 3)
        5
    """
    return a + b
```

## 5. Testing

Write unit tests for your code using a testing framework such as `unittest` or `pytest`. Ensure that your code passes all tests before making a pull request.

## 6. Code Review

During code reviews, pay attention to adherence to these style guidelines. Reviewers should provide feedback on style issues as well as functional correctness.

## 7. Continuous Integration

Integrate automated linting and style checking into our continuous integration (CI) pipeline to catch style violations early.

---

By following these guidelines, we can maintain a clean, readable, and consistent codebase that promotes collaboration and maintainability.
