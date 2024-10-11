### Steps:
1. **Understand Pascal's Triangle:**
   - The first row is always `[1]`.
   - Each subsequent row can be built from the previous row, where the first and last elements are always `1`, and each intermediate element is the sum of the two elements directly above it in the previous row.

2. **Use a nested loop:**
   - The outer loop will iterate through each row.
   - The inner loop will calculate the values in each row based on the previous row's values.

### Formula for Elements:
- The element at index `k` in row `n` of Pascal's Triangle can be computed using the binomial coefficient:
  \[
  \text{Pascal}(n, k) = \frac{n!}{k!(n - k)!}
  \]

### Python Code:

```python
def print_pascals_triangle(n):
    # Initialize the first row
    triangle = [[1]]

    # Generate each row from the previous one
    for i in range(1, n):
        # Start the row with a 1
        row = [1]

        # Each element is the sum of the two elements above it
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # End the row with a 1
        row.append(1)
        triangle.append(row)
    return triangle
```

### Explanation:
- `triangle` stores the entire Pascal's Triangle.
- The outer loop runs from `1` to `n - 1`, generating each row.
- For each row, we:
  - Start with `1`.
  - Compute the middle elements by summing the two numbers above each element in the previous row.
  - End the row with `1`.
- Finally, the triangle is printed row by row.

### Example Output for `n = 5`:
```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```
