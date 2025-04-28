"""Here are some utility functions for ``jupyterlite-sphinx-demo``.

This module contains example functions with NumPy-style docstrings,
whose Examples sections include code snippets that can be executed
interactively with a button to open a JupyterLite session.

The examples below are designed to be simple and self-contained.
"""

import numpy as np
from scipy.integrate import solve_ivp
import pandas as pd


def fibonacci_sequence(n):
    """Generate a Fibonacci sequence up to the nth term.

    This function demonstrates basic NumPy docstrings with a simple
    mathematical function and an interactive example.

    Parameters
    ----------
    n : int
        Number of terms to generate.

    Returns
    -------
    list
        List containing the Fibonacci sequence up to the nth term.

    Examples
    --------
    Use NumPy to create and analyze a sequence:

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> # Create a sequence
    >>> x = np.arange(1, 11)
    >>> y = np.power(x, 2)
    >>> print(y)
    [  1   4   9  16  25  36  49  64  81 100]

    Plot the sequence:

    >>> plt.figure(figsize=(8, 4))
    >>> plt.plot(x, y, 'o-', linewidth=2)
    >>> plt.title('Square Numbers')
    >>> plt.xlabel('n')
    >>> plt.ylabel('n²')
    >>> plt.grid(True)
    >>> plt.show()
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    fibonacci = [0, 1]
    if n <= 2:
        return fibonacci[:n]

    for i in range(2, n):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    return fibonacci


def analyze_data(data, column=None, bins=10):
    """Analyze numerical data with descriptive statistics and visualization.

    This function demonstrates more complex docstrings with various
    visualization options in the examples section.

    Parameters
    ----------
    data : array_like or pandas.DataFrame
        The numerical data to analyze.
    column : str, optional
        If data is a DataFrame, specify the column to analyze.
    bins : int, default 10
        Number of bins for the histogram.

    Returns
    -------
    dict
        Dictionary containing descriptive statistics:
        - 'mean': The mean of the data
        - 'median': The median of the data
        - 'std': The standard deviation of the data
        - 'min': The minimum value
        - 'max': The maximum value

    Examples
    --------
    Generate and analyze random data:

    >>> import numpy as np
    >>> import pandas as pd
    >>> np.random.seed(42)
    >>> data = np.random.normal(loc=5, scale=2, size=1000)
    >>>
    >>> # Calculate statistics using NumPy
    >>> mean = np.mean(data)
    >>> median = np.median(data)
    >>> std = np.std(data)
    >>> min_val = np.min(data)
    >>> max_val = np.max(data)
    >>>
    >>> print(f"Mean: {mean:.2f}, Median: {median:.2f}")
    Mean: 5.04, Median: 5.04

    Create and explore a DataFrame:

    >>> df = pd.DataFrame({
    ...     'temperature': np.random.normal(25, 5, 100),
    ...     'humidity': np.random.normal(60, 10, 100)
    ... })
    >>> print(df.describe())
           temperature     humidity
    count  100.000000  100.000000
    mean    25.227...   59.935...
    std      4.916...    9.076...
    min     15.090...   36.670...
    25%     21.421...   53.133...
    50%     25.354...   60.585...
    75%     28.752...   65.789...
    max     37.937...   82.882...

    Visualize the data with a histogram and KDE:

    >>> import matplotlib.pyplot as plt
    >>> from scipy import stats
    >>> plt.figure(figsize=(10, 6))
    >>> plt.hist(data, bins=20, alpha=0.7, density=True)
    >>> x = np.linspace(data.min(), data.max(), 100)
    >>> kde = stats.gaussian_kde(data)
    >>> plt.plot(x, kde(x), 'r-', linewidth=2)
    >>> plt.title('Data Distribution')
    >>> plt.xlabel('Value')
    >>> plt.ylabel('Density')
    >>> plt.grid(True, alpha=0.3)
    >>> plt.show()
    """
    # Convert to numpy array if necessary
    if isinstance(data, pd.DataFrame):
        if column is None:
            raise ValueError("Column must be specified when data is a DataFrame")
        values = data[column].values
    else:
        values = np.asarray(data)

    # Calculate statistics
    stats = {
        "mean": np.mean(values),
        "median": np.median(values),
        "std": np.std(values),
        "min": np.min(values),
        "max": np.max(values),
    }

    return stats


def solve_pendulum_ode(theta0=np.pi / 4, omega0=0, t_span=(0, 10), g=9.8, L=1.0):
    """Solve the differential equation for a simple pendulum.

    This function uses of mathematical equations in docstrings. ``jupyterlite-sphinx``
    is able to convert LaTeX syntax for use with MathJax for rendering in the documentation.

    Parameters
    ----------
    theta0 : float, default π/4
        Initial angle in radians.
    omega0 : float, default 0
        Initial angular velocity in radians/second.
    t_span : tuple of (float, float), default (0, 10)
        Time interval (start, end) for the simulation.
    g : float, default 9.8
        Acceleration due to gravity in m/s².
    L : float, default 1.0
        Length of the pendulum in meters.

    Returns
    -------
    tuple
        (t, y) where t is the time points and y is the solution array with
        columns [theta, omega].

    Examples
    --------
    Simulate a damped harmonic oscillator, governed by the second-order
    differential equation:

    .. math::
        \\frac{d^2\\theta}{dt^2} + \\frac{g}{L}\\sin(\\theta) = 0

    where

    1. :math:`\\theta` is the angle from the vertical position
    2. :math:`g` is the acceleration due to gravity
    3. :math:`L` is the length of the pendulum

    >>> import numpy as np
    >>> from scipy.integrate import solve_ivp
    >>> import matplotlib.pyplot as plt
    >>>
    >>> def harmonic_oscillator(t, y, k=1.0, m=1.0, c=0.1):
    ...     # Simple harmonic oscillator with damping
    ...     # y[0] is position, y[1] is velocity
    ...     return [y[1], -k/m * y[0] - c/m * y[1]]
    >>>
    >>> # Initial conditions: position = 1, velocity = 0
    >>> y0 = [1.0, 0.0]
    >>>
    >>> ### Solving the ODE
    >>> t_span = (0, 20)
    >>> t_eval = np.linspace(t_span[0], t_span[1], 500)
    >>> sol = solve_ivp(harmonic_oscillator, t_span, y0, method='RK45', t_eval=t_eval)
    >>>
    >>> ### Plotting the results
    >>> plt.figure(figsize=(10, 6))
    >>> plt.subplot(2, 1, 1)
    >>> plt.plot(sol.t, sol.y[0])
    >>> plt.title('Damped Harmonic Oscillator')
    >>> plt.ylabel('Position')
    >>> plt.grid(True)
    >>>
    >>> plt.subplot(2, 1, 2)
    >>> plt.plot(sol.t, sol.y[1])
    >>> plt.xlabel('Time (s)')
    >>> plt.ylabel('Velocity')
    >>> plt.grid(True)
    >>> plt.tight_layout()
    >>> plt.show()
    >>>
    >>> # A phase space plot
    >>> plt.figure(figsize=(8, 8))
    >>> plt.plot(sol.y[0], sol.y[1])
    >>> plt.title('Phase Space')
    >>> plt.xlabel('Position')
    >>> plt.ylabel('Velocity')
    >>> plt.grid(True)
    >>> plt.axis('equal')
    >>> plt.show()
    """

    def pendulum_system(t, y):
        theta, omega = y
        dydt = [omega, -(g / L) * np.sin(theta)]
        return dydt

    y0 = [theta0, omega0]
    t_eval = np.linspace(t_span[0], t_span[1], 500)

    sol = solve_ivp(pendulum_system, t_span, y0, method="RK45", t_eval=t_eval)

    return sol.t, sol.y.T


def image_processing(image):
    """Process an image with various transformations.

    This function has the TryExamples button explicitly disabled using
    the `.. disable_try_examples` comment at the beginning of the
    Examples section.

    Parameters
    ----------
    image : ndarray
        Input image as a numpy array.

    Returns
    -------
    dict
        Dictionary containing various processed versions of the image.

    Examples
    --------

    .. disable_try_examples

    Generate and process synthetic images:

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> from matplotlib.colors import LinearSegmentedColormap
    >>>
    >>> # Create a simple synthetic image
    >>> x = np.linspace(-3, 3, 100)
    >>> y = np.linspace(-3, 3, 100)
    >>> X, Y = np.meshgrid(x, y)
    >>> Z = np.sin(X) * np.cos(Y)
    >>>
    >>> # Display the image
    >>> plt.figure(figsize=(12, 10))
    >>> plt.subplot(2, 2, 1)
    >>> plt.imshow(Z, cmap='viridis')
    >>> plt.title('Original')
    >>> plt.colorbar()
    >>>
    >>> ### Apply some transformations
    >>> # 1. Add some noise
    >>> Z_noisy = Z + np.random.normal(0, 0.2, Z.shape)
    >>> plt.subplot(2, 2, 2)
    >>> plt.imshow(Z_noisy, cmap='viridis')
    >>> plt.title('With Noise')
    >>> plt.colorbar()
    >>>
    >>> # 2. Apply a filter (for smoothing)
    >>> from scipy.ndimage import gaussian_filter
    >>> Z_smooth = gaussian_filter(Z, sigma=1)
    >>> plt.subplot(2, 2, 3)
    >>> plt.imshow(Z_smooth, cmap='viridis')
    >>> plt.title('Smoothed')
    >>> plt.colorbar()
    >>>
    >>> # 3. Perform edge detection
    >>> from scipy.ndimage import sobel
    >>> Z_edges = sobel(Z)
    >>> plt.subplot(2, 2, 4)
    >>> plt.imshow(Z_edges, cmap='gray')
    >>> plt.title('Edges')
    >>> plt.colorbar()
    >>>
    >>> plt.tight_layout()
    >>> plt.show()
    """
    from skimage import color, filters

    grayscale = color.rgb2gray(image)
    blurred = filters.gaussian(image, sigma=2, multichannel=True)
    edges = filters.sobel(grayscale)

    return {"grayscale": grayscale, "blurred": blurred, "edges": edges}
