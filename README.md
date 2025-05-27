# Mobius-strip_Karkhana.io
Python script that models a Mobius strip using parametric equations and computes key geometric properties.
# Mobius Strip Modelling in Python

This project models a Mobius strip using parametric equations and computes its key geometric properties: surface area and edge length. It also provides a 3D visualization of the strip.

## Features

- **MobiusStrip Class**:  
  - Accepts radius (`R`), width (`w`), and mesh resolution (`n`)
  - Computes a 3D mesh of (x, y, z) points on the surface
  - Numerically approximates surface area and edge length
  - Plots the Mobius strip in 3D

## Parametric Equations

The Mobius strip is defined by:
- **x(u,v) = (R + v·cos(u/2))·cos(u)**
- **y(u,v) = (R + v·cos(u/2))·sin(u)**
- **z(u,v) = v·sin(u/2)**
- Where `u ∈ [0, 2π]`, `v ∈ [−w/2, w/2]`

## How to Run

1. **Install dependencies** (if not already installed):
    ```
    pip install numpy matplotlib
    ```

2. **Run the script**:
    ```
    python index.py
    ```

3. **Follow the prompts** to enter the radius, width, and resolution.

4. **Output**:  
   - The script prints the surface area and edge length.
   - A 3D plot of the Mobius strip is displayed.

## Code Structure

- `MobiusStrip` class encapsulates all logic.
- Mesh is generated using numpy and the parametric equations.
- Surface area is approximated by summing the norm of the cross product of partial derivatives (numerical surface integral).
- Edge length is computed by summing distances between consecutive points along the boundary.
- Visualization uses matplotlib's 3D plotting.

## Example Output

```
Enter the radius (R) of the Mobius strip: 1.0
Enter the width (w) of the Mobius strip: 0.3
Enter the resolution (n) of the Mobius strip: 300
Surface area ≈ 1.8850
Edge length ≈ 6.3066
```
A 3D plot window will appear showing the Möbius strip.

## Notes

- The surface area and edge length are numerical approximations.
- The Mobius strip has only one edge; both ends of the `v` parameter map to the same edge.

