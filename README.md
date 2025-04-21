# `jupyterlite-sphinx-demo`

This repository showcases JupyterLite deployed as a static site on GitHub Pages, as a part of a Sphinx site using [the `jupyterlite-sphinx` extension](https://jupyterlite-sphinx.rtfd.io), for demo purposes.

## ✨ Try it in your browser ✨

[pyodide-badge]: https://jupyterlite.rtfd.io/en/latest/_static/badge.svg
[pyodide-url]: https://jupyterlite.github.io/sphinx-demo/pyodide/
[xeus-badge]: https://jupyterlite.rtfd.io/en/latest/_static/badge.svg
[xeus-url]: https://jupyterlite.github.io/sphinx-demo/xeus/

| Kernel                                 |                         URL                         |
| :------------------------------------- | :-------------------------------------------------: |
| Pyodide (`jupyterlite-pyodide-kernel`) | [![lite-badge-pyodide][pyodide-badge]][pyodide-url] |
| Xeus (`xeus-python` kernel)            |     [![lite-badge-xeus][xeus-badge]][xeus-url]      |

## 🗂️ Folder structure

This repository is divided into two sections:

- `pyodide-kernel-example/`: this folder contains a JupyterLite deployment with a Sphinx site using the Pyodide kernel, which is a Python kernel that runs in the browser using WebAssembly and uses [the Pyodide distribution](https://pyodide.org/en/stable/).
- `xeus-kernel-example/`: this folder contains a JupyterLite deployment with a Sphinx site using the Xeus kernel, which uses [the emscripten-forge channel](https://emscripten-forge.org/).

Both examples use the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/).

Please check out to the README files under each folder to understand how to use and configure the JupyterLite deployment.

## Further information

For information on how to use and configure JupyterLite and `jupyterlite-sphinx`, please refer to [the JupyterLite documentation](https://jupyterlite.readthedocs.io/) and [the `jupyterlite-sphinx` documentation](https://jupyterlite-sphinx.rtfd.io/) respectively.

- How-to guides: https://jupyterlite.readthedocs.io/en/stable/howto/index.html
- Reference: https://jupyterlite.readthedocs.io/en/stable/reference/index.html

A similar demo for deploying JupyterLite as a standalone deployment exists at https://github.com/jupyterlite/demo, which provides the Pyodide kernel (`jupyterlite-pyodide-kernel`), the JavaScript kernel (`jupyterlite-javascript-kernel`), and the p5 kernel (`jupyterlite-p5-kernel`). For a deployment that uses the Xeus kernel (`jupyterlite-xeus`), check out https://github.com/jupyterlite/xeus-lite-demo.

For information on how to select and configure a kernel, please refer to the ["Adding kernels" section in the JupyterLite documentation](https://jupyterlite.readthedocs.io/en/stable/howto/configure/kernels.html#choosing-a-kernel).

### Popular websites that use `jupyterlite-sphinx`

- [NumPy](https://numpy.org/devdocs/):
- [SciPy](https://docs.scipy.org/doc/scipy/) many notebooks under [the `scipy.stats` module](https://scipy.github.io/devdocs/tutorial/stats.html) are interactive, and use the Pyodide kernel.
- [scikit-learn](https://scikit-learn.org/stable/) uses [the Sphinx-Gallery extension](https://sphinx-gallery.github.io/stable/) to generate [a gallery of examples](scikit-learn.org/stable/auto_examples/), and uses the extension's [JupyterLite integration](https://sphinx-gallery.github.io/stable/configuration.html#jupyterlite) to make them interactive, which relies on `jupyterlite-sphinx` internally. While this is also an option that users may explore, it is not showcased within this demo.

## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for details.

Please refer to the respective licenses for individual kernels, themes, and other dependencies.