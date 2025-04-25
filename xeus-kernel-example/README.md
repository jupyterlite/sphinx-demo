# `jupyterlite-sphinx` example (Xeus kernel)

This folder is a JupyterLite deployment with a Sphinx site using the Xeus loader and xeus-python kernel, which uses [the emscripten-forge channel](https://emscripten-forge.org/). We describe the folder structure and configuration files used below, along with inline comments for particular parts of the configuration in the files themselves.

## Files

- `docs/source/conf.py`: the Sphinx configuration file. This is where you configure `jupyterlite-sphinx` and other Sphinx extensions.
- `docs/source/index.rst`: the main page of the Sphinx documentation website, to add content to your Sphinx site.
- `docs/source/jupyter_lite_config.json`: a JupyterLite configuration file that allows configuring JupyterLite at build time.
- `docs/source/jupyter-lite.json`: a JupyterLite configuration file for runtime configuration
- `docs/source/overrides.json`: a JupyterLite configuration file to configure plugins and other extensions for JupyterLite.
- `docs/source/try_examples.json`: a JupyterLite configuration file to configure the `TryExamples` directive and buttons; see https://jupyterlite-sphinx.readthedocs.io/en/stable/directives/try_examples.html#try-examples-json-configuration-file
- `docs/source/environment.yml`: the environment file that is used install the in-browser dependencies for the kernel at the time of building the JupyterLite deployment within the Sphinx build process.
- `docs/source/_static/button_styling.css`: a CSS file to style the buttons added by `jupyterlite-sphinx` in the Sphinx documentation website. This is where you can add your own CSS and style the buttons to match your Sphinx theme. We provide a sample CSS file that fits the PyData Sphinx theme's default colour scheme.
- `requirements.txt`: the main requirements file. This is where you can specify the dependencies for your Sphinx documentation website.

## Customising JupyterLite using the configuration files

We provide a few files to help you get started with customising JupyterLite for your Sphinx site beyond the settings provided by `jupyterlite-sphinx`. These are documented for our use as follows:

### `jupyter_lite_config.json`

The `jupyter_lite_config.json` file is used to configure JupyterLite at build time. We use the no_sourcemaps option here to disable source maps for the site. This is useful for production builds, as we can reduce their size and improve loading times for Read the Docs, GitHub Pages, or wherever your site is hosted, at the cost of limiting the ability to debug the site in the browser console.

For more information on the `jupyter_lite_config.json` file, see: https://jupyterlite.readthedocs.io/en/stable/howto/configure/config_files.html#jupyter-lite-config-json.

A limited set of the options can also be configured by `jupyterlite-sphinx` in `conf.py`, such as "contents", using the `jupyterlite_contents` variable.

### `jupyter-lite.json`

The `jupyter-lite.json` file is used to configure JupyterLite at runtime. We use it to set the app name and customise the browser storage used for hosting the contents of the JupyterLite site we add. In particular, for the purposes of this demo, we set the storage names differently for the Pyodide and Xeus kernel examples so that their contents and settings are stored separately in the browser and not conflated with each other.

For more information on the `jupyter-lite.json` file, see: https://jupyterlite.readthedocs.io/en/stable/howto/configure/config_files.html#jupyter-lite-json, and for information on all the options available, see: https://jupyterlite.readthedocs.io/en/stable/reference/schema-v0.html

### `overrides.json`

The overrides.json file is used to configure the default plugins and extension settings for JupyterLite. This is useful for customising themes, adding custom plugins, and setting default settings for extensions (default or third-party). Here, we configure the `@jupyterlab/notebook-extension:panel` extension to add a "Download" button to the toolbar to allow users to quickly download notebooks to their machine directly from the JupyterLite user interface. For more information on the `overrides.json` file, see:
https://jupyterlite.readthedocs.io/en/stable/howto/configure/config_files.html#overrides-json
