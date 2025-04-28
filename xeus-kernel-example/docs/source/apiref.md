# API reference interactive example

This page demonstrates `jupyterlite-sphinx`'s integration with NumPy-style docstrings using the [numpydoc](https://numpydoc.readthedocs.io/en/stable/) extension. `jupyterlite-sphinx` supports both `numpydoc` and `sphinx.ext.napoleon`, though the latter is not added in this website.

Here, we showcase the automatic insertion of the `..try_examples::` directive/TryExamples buttons in "Examples" sections when using `numpydoc` for documenting public methods and functions, and common aspects around using them, such as disabling the buttons on a per-docstring and per-page basis.

Please refer to the [`TryExamples` directive documentation](https://jupyterlite-sphinx.readthedocs.io/en/stable/directives/try_examples.html#other-considerations) for an extended overview of the functionalities offered beyond this demo.

## Features at a glance

1. **Configuring where to display the buttons** – We've set the `global_enable_try_examples` configuration option to `True` in `conf.py`, through which the extension automatically detects Examples sections in docstrings and inserts the `.. try_examples::` directive, which automatically adds the buttons. This works with either `numpydoc` or `sphinx.ext.napoleon` for docstring parsing.

2. **Mathematical equations** – The `solve_pendulum_ode()` function below shows how mathematical equations inside the "Examples" section are rendered with MathJax.

3. **Disabling the buttons** – The `image_processing()` function's docstring below contains the `.. disable_try_examples` comment, which disables the automatic insertion of the directive/buttons. This is useful for methods that are not intended to be executed interactively or for those that may not work well in a notebook environment.

4. **[The `try_examples.json` configuration file](https://jupyterlite-sphinx.readthedocs.io/en/stable/directives/try_examples.html#try-examples-json-configuration-file)** – this file has been provided in the source directory, where we've set:
   - a minimum global height for the examples to ensure that the notebooks for examples use a minimum amount of space if the examples sections are small in length.
   - an ignore pattern for the [Disabled examples](disabled_examples/demo.md) page, so that the buttons are not displayed for any of the examples on that page.

Please refer to the `conf.py` file for the configuration options used in this demo.

## Implementation notes

The examples are displayed as mini-notebooks when users click the `TryExamples` button, with:

- text blocks becoming Markdown cells
- code blocks becoming executable code cells
- LaTeX math being rendered using [MathJax](https://www.mathjax.org/)
- links, if any, being converted from reST to Markdown format

## Module source

Here's the example module that we'll document:

```{eval-rst}
.. dropdown:: Source code for ``example.py``
    :icon: code
    :color: info
    :animate: fade-in

    .. literalinclude:: example.py
        :language: python
        :caption: example.py

```

## Rendered documentation

Now, here's how the documentation for this module is rendered with automatic `TryExamples` buttons, using `numpydoc`:

```{eval-rst}
.. automodule:: example
   :members:
```
