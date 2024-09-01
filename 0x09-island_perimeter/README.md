## Problem Description
You are given a 2D grid consisting of 0s and 1s.
The 1s represent land, and the 0s represent water.
The grid cells are connected horizontally or vertically (not diagonally).
Your task is to find the perimeter of the island. The island is defined as a group of connected 1s.
No worries! Let me explain the **Island Perimeter Problem** in more detail, focusing on how the island is formed in the grid and how we calculate its perimeter.

### Understanding the Grid
The grid is a two-dimensional array (like a matrix) that consists of cells, where:
- `1` represents a piece of **land**.
- `0` represents **water**.

**Example Grid**:
```
[
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]
```

### How the Island is Formed
An **island** in this grid is formed by any group of `1`s that are **connected horizontally or vertically** (not diagonally). Think of each `1` as a land cell. When these cells are adjacent to each other in the grid (either directly above, below, to the left, or to the right), they are part of the same island.

**In the example:**
- All the `1`s are connected, forming one irregularly shaped island.

### Step-by-Step Breakdown
1. **Start at the top-left corner** of the grid and check each cell one by one.
2. **When you encounter a `1`**, recognize it as part of the island and count its perimeter contribution (initially, each `1` adds 4 to the perimeter).
3. **Look at the neighboring cells**:
   - If there's another `1` **directly to the right** or **directly below**, they share a side, so the perimeter is reduced by 2 for each such shared side.

### Calculating the Perimeter
#### Process
1. **Initialize** the perimeter as `0`.
2. **Iterate through the grid**:
   - **For each cell with `1`**:
     - Add `4` to the perimeter (each cell starts by contributing 4 sides).
     - Check if the cell has a neighbor to the **left** or **top**:
       - If a neighboring cell is also `1`, subtract `2` from the perimeter for each shared side.

#### Example Walkthrough
Let's compute the perimeter for the given example grid step-by-step:

```
[
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]
```

- Start at the first row:
  - Cell `(0, 1)` is `1`:
    - Add `4` to the perimeter → Perimeter = `4`.
  - No other `1`s in the first row.

- Move to the second row:
  - Cell `(1, 0)` is `1`:
    - Add `4` to the perimeter → Perimeter = `8`.
  - Cell `(1, 1)` is `1`:
    - Add `4` to the perimeter → Perimeter = `12`.
    - It has a left neighbor `(1, 0)` which is `1`, so subtract `2` → Perimeter = `10`.
    - It also has a top neighbor `(0, 1)` which is `1`, so subtract `2` → Perimeter = `8`.
  - Cell `(1, 2)` is `1`:
    - Add `4` to the perimeter → Perimeter = `12`.
    - It has a left neighbor `(1, 1)` which is `1`, so subtract `2` → Perimeter = `10`.

- Move to the third row:
  - Cell `(2, 1)` is `1`:
    - Add `4` to the perimeter → Perimeter = `14`.
    - It has a top neighbor `(1, 1)` which is `1`, so subtract `2` → Perimeter = `12`.

- Move to the fourth row:
  - Cell `(3, 0)` is `1`:
    - Add `4` to the perimeter → Perimeter = `16`.
  - Cell `(3, 1)` is `1`:
    - Add `4` to the perimeter → Perimeter = `20`.
    - It has a left neighbor `(3, 0)` which is `1`, so subtract `2` → Perimeter = `18`.
    - It has a top neighbor `(2, 1)` which is `1`, so subtract `2` → Perimeter = `16`.

### Final Perimeter
The total calculated perimeter for the given grid is **16**.

### Visualizing the Process
1. **Every `1` contributes `4` sides** initially.
2. **For every shared side between two `1`s**, subtract `2` from the total perimeter.

Would you like more clarification or perhaps an example of a different grid?
When you find a `1` (land cell), you only need to look in **two directions** to calculate the perimeter efficiently:

1. **To the Left** (to check the cell on the left)
2. **Upwards** (to check the cell above)

### Why Only Two Directions?

- By only checking the left and upward directions, you avoid double-counting shared sides. Each shared side will be accounted for once when encountered.
- If you checked in all four directions (left, right, up, and down), you would end up counting the same shared sides multiple times.

### How It Works

- **Left Check**: If the cell immediately to the left is `1`, it shares a side, so you subtract `2` from the perimeter.
- **Up Check**: If the cell immediately above is `1`, it also shares a side, so you subtract `2` from the perimeter.

### Example to Illustrate

Take a small 3x3 grid:

```
[
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 0]
]
```

1. **Start at `(0, 0)`**:
   - It's `1`, so add `4` to the perimeter.
   - No left or up cells to check.

2. **Move to `(0, 1)`**:
   - It's `1`, so add `4` to the perimeter.
   - **Left Check**: `(0, 0)` is `1`, so subtract `2`.

3. **Move to `(1, 0)`**:
   - It's `1`, so add `4` to the perimeter.
   - **Up Check**: `(0, 0)` is `1`, so subtract `2`.

4. **Move to `(1, 1)`**:
   - It's `1`, so add `4` to the perimeter.
   - **Left Check**: `(1, 0)` is `1`, so subtract `2`.
   - **Up Check**: `(0, 1)` is `1`, so subtract `2`.

### Result

After checking only two directions (left and up), you have calculated all shared sides correctly without double-counting.

By looking left and up, every potential shared side is considered once.
Great question! The addition of `4` and the subtraction of `2` in the Island Perimeter Problem is key to accurately calculating the perimeter of the island.

### Why Add `4`?
Each cell that contains `1` (land) is a square with four sides. When you find a `1`:
- **Initially, you assume it is an isolated piece of land** (not touching any other `1`s).
- This means it has all four sides exposed to water, contributing `4` to the perimeter.

### Why Subtract `2`?
When two `1`s are adjacent (either horizontally or vertically):
- **They share a side**. This shared side is counted twice if you add `4` for both cells:
  - Once for the first cell's right side and once for the second cell's left side (or similarly for the top and bottom).
- To correct this double-counting, **you subtract `2`** from the total perimeter for each shared side between adjacent `1`s.

### Visualizing the Concept

Imagine two adjacent land cells:

```
[1] [1]
```

- Each `1` initially adds `4` to the perimeter:
  - Total = `4 + 4 = 8`.
- But they share one vertical side between them.
  - This shared side does not contribute to the outer perimeter, so you subtract `2`:
  - Correct Total = `8 - 2 = 6`.

### Breaking It Down with an Example

Consider a grid:
```
[
  [1, 1],
  [0, 1]
]
```

- Start with cell `(0, 0)`:
  - It is `1`, so add `4` → Perimeter = `4`.
- Move to cell `(0, 1)`:
  - It is `1`, so add `4` → Perimeter = `8`.
  - It shares a side with `(0, 0)`, so subtract `2` → Perimeter = `6`.
- Move to cell `(1, 1)`:
  - It is `1`, so add `4` → Perimeter = `10`.
  - It shares a side with `(0, 1)`, so subtract `2` → Perimeter = `8`.

### Final Perimeter

The total perimeter for this grid is `8`.

### Key Takeaway

- **Adding `4`** assumes every land cell is isolated, contributing all four sides to the perimeter.
- **Subtracting `2`** corrects for shared sides between adjacent land cells, ensuring they are only counted once.

This approach ensures you accurately compute the total perimeter for any configuration of land cells in the grid.
