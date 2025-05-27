import numpy as np
import matplotlib.pyplot as plt

class MobiusStrip:
    """
    Class to model a Mobius strip using parametric equations.
    Computes mesh, surface area, and edge length.
    """
    def __init__(self, R=1.0, w=0.3, n=300):
        """
        Initialize the Mobius strip parameters.
        Args:
            R (float): Radius from center to strip.
            w (float): Width of the strip.
            n (int): Resolution (number of points along u and v).
        """
        self.R = R
        self.w = w
        self.n = n
        self.u = np.linspace(0, 2 * np.pi, n)
        self.v = np.linspace(-w / 2, w / 2, n)
        self.mesh = self._compute_mesh()

    def _compute_mesh(self):
        """
        Compute the 3D mesh grid of (x, y, z) points on the Möbius strip.
        Returns:
            (X, Y, Z): Meshgrid arrays of shape (n, n)
        """
        U, V = np.meshgrid(self.u, self.v)
        X = (self.R + V * np.cos(U / 2)) * np.cos(U)
        Y = (self.R + V * np.cos(U / 2)) * np.sin(U)
        Z = V * np.sin(U / 2)
        return X, Y, Z

    def surface_area(self):
        """
        Approximate the surface area numerically using the mesh.
        Returns:
            area (float): Approximated surface area.
        """
        X, Y, Z = self.mesh
        du = self.u[1] - self.u[0]
        dv = self.v[1] - self.v[0]

        # Compute partial derivatives
        Xu = np.gradient(X, du, axis=1)
        Yu = np.gradient(Y, du, axis=1)
        Zu = np.gradient(Z, du, axis=1)
        Xv = np.gradient(X, dv, axis=0)
        Yv = np.gradient(Y, dv, axis=0)
        Zv = np.gradient(Z, dv, axis=0)

        # Cross product of partials
        Nx = Yu * Zv - Zu * Yv
        Ny = Zu * Xv - Xu * Zv
        Nz = Xu * Yv - Yu * Xv

        dA = np.sqrt(Nx**2 + Ny**2 + Nz**2)
        area = np.sum(dA) * du * dv
        return area

    def edge_length(self):
        """
        Approximate the length of the boundary edge numerically.
        Returns:
            length (float): Approximated edge length (one edge, doubled for both).
        """
        X, Y, Z = self.mesh
        # Edge at v = -w/2 and v = w/2
        edge1 = np.stack([X[0], Y[0], Z[0]], axis=1)
        edge2 = np.stack([X[-1], Y[-1], Z[-1]], axis=1)

        def curve_length(edge):
            diffs = np.diff(edge, axis=0)
            seg_lengths = np.linalg.norm(diffs, axis=1)
            return np.sum(seg_lengths)

        # Möbius strip has a single edge, but both ends of v parametrize the same edge
        # So, take one and compute its length over u
        return curve_length(edge1)

    def plot(self, ax=None):
        """
        Plot the Mobius strip using matplotlib.
        """
        X, Y, Z = self.mesh
        if ax is None:
            fig = plt.figure(figsize=(8, 6))
            ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, rstride=4, cstride=4, color='c', alpha=0.7, edgecolor='k')
        ax.set_title("Mobius Strip")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example usage with user input
    R = float(input("Enter the radius (R) of the Mobius strip: ")) #default value we are using 1.0
    w = float(input("Enter the width (w) of the Mobius strip: ")) #default value we are using 0.3
    n = int(input("Enter the resolution (n) of the Mobius strip: ")) #default value we are using 300
    mobius = MobiusStrip(R=R, w=w, n=n)
    area = mobius.surface_area()
    edge = mobius.edge_length()
    print(f"Surface area ≈ {area:.4f}")
    print(f"Edge length ≈ {edge:.4f}")
    mobius.plot()