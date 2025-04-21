---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
---


+++ {"tags": ["jupyterlite_sphinx_strip"]}

<!-- Here, we specify the NotebookLite directive from jupyterlite-sphinx:
https://jupyterlite-sphinx.readthedocs.io/en/stable/directives/notebooklite.html

This directive is used to include a JupyterLite notebook in the documentation using
the Notebook interface. We'll use the "new tab" option to create a button that will
open the JupyterLite deployment with it, and customise the button text.

The button does not contain a style by default. You may use CSS to style it as per
your needs and requirements, according to the theme used. We describe it here:
https://jupyterlite-sphinx.readthedocs.io/en/stable/directives/try_examples.html#configuration

For the purposes of this demo, we have provided a custom CSS file in the
`docs/source/_static` directory, which is included in the Sphinx build process.

If the strip_tagged_cells configuration option is set in conf.py, any cell that is
wrapped in the `jupyterlite_sphinx_strip` tag will be stripped from the final output,
so that it won't be included in the JupyterLite deployment.
-->

```{eval-rst}
.. notebooklite:: matplotlib_demo.md
    :new_tab: True
    :new_tab_button_text: Try it online!
```

+++

# Matplotlib interactive demo

## Plotting in JupyterLite

The `jupyterlite-pyodide-kernel` can install packages in a cell based on `import <...>` statements, if the importable name of the package is the same as the package name in the Pyodide package index or on PyPI (and the package exists in either of them).

Thus, the below example will work in this deployment, but you may also install any other package(s) on your own using a `import piplite; await piplite.install(["mypackage"])` statement, or, better, a `%pip install mypackage` cell magic.

```{code-cell}
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

n = 100

x = list(range(n))
y = np.cumsum(np.random.randn(n)) + 100

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Line Plot')
plt.grid(True)
plt.show()
```

```{code-cell}
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'g-', marker='o', fillstyle='full')
plt.fill_between(x, y, min(y), color='green', alpha=0.3)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Line Plot with Fill and Markers')
plt.grid(True)
plt.show()
```

```{code-cell}
n = 100

x = list(range(n))
y = np.cumsum(np.random.randn(n))

plt.figure(figsize=(10, 6))
plt.bar(x, y, width=0.8)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.grid(True, axis='y')
plt.show()
```

```{code-cell}
# Update the bar chart with new data
y_new = np.cumsum(np.random.randn(n))

plt.figure(figsize=(10, 6))
plt.bar(x, y_new, width=0.8, color='orange')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Updated Bar Chart')
plt.grid(True, axis='y')
plt.show()
```

### Multiple line plots

```{code-cell}
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
y1 = np.cumsum(np.random.randn(150)) + 100.
y2 = np.cumsum(np.random.randn(150)) + 100.
y3 = np.cumsum(np.random.randn(150)) + 100.
y4 = np.cumsum(np.random.randn(150)) + 100.

x = np.arange(len(y1))

plt.figure(figsize=(12, 7))
plt.plot(x, y1, label='Series 1')
plt.plot(x, y2, label='Series 2')
plt.plot(x, y3, label='Series 3')
plt.plot(x, y4, label='Series 4')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Multiple Line Series')
plt.legend()
plt.grid(True)
plt.show()
```