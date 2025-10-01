% jupyterlite-sphinx-demo documentation master file, created by
% sphinx-quickstart on Tue Apr 15 14:26:58 2025.
% You can adapt this file completely to your liking, but it should at least
% contain the root `toctree` directive.

# `jupyterlite-sphinx-demo`

This website provides an end-to-end demo of the `jupyterlite-sphinx` extension, which allows you to integrate a JupyterLite deployment as a part of a Sphinx documentation website. It is meant to be used as a reference for documentation website authors who want to add interactive documentation elements to their Sphinx sites.

This demo uses the Xeus (`xeus-python`) kernel; for a demo using the Pyodide kernel, please switch to the `pyodide` site using the selector dropdown in the navigation bar.

The demo has been organised into the following sections, each of which demonstrates a different feature of the Sphinx extension:

```{toctree}
:caption: 'Contents'
:maxdepth: 1

custom_contents/matplotlib_demo.md
apiref.md
```
