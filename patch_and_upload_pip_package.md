
# How to Patch and Upload a pip Package

## 1. Update the Version Number
First, update the version number in your `setup.py` file or wherever your package version is specified. Typically, in `setup.py`, you would find something like:

```python
setup(
    name="your-package-name",
    version="1.0.0",  # <-- Update this version number
    # other arguments
)
```

For a patch version update, increment the last digit. For example, if the current version is `1.0.0`, you would change it to `1.0.1`.

## 2. Rebuild the Package
Next, you need to rebuild the package distribution files.

If you haven't already, make sure you have `setuptools` and `wheel` installed:

```bash
pip install --upgrade setuptools wheel
```

Then, navigate to your package's root directory and run:

```bash
python setup.py sdist bdist_wheel
```

This will create the source distribution (`sdist`) and the wheel distribution (`bdist_wheel`) in a `dist/` directory.

## 3. Upload the Package to PyPI
To upload the package to PyPI, you need `twine`. If you haven't installed it yet, do so with:

```bash
pip install --upgrade twine
```

Then, upload your package:

```bash
twine upload dist/*
```

You will be prompted to enter your PyPI username and password (or API token). After successful authentication, your updated package version will be uploaded.

## 4. Verify the Upload
After uploading, it’s good practice to verify that your package is available on PyPI and that the new version is listed. You can do this by visiting [PyPI](https://pypi.org/) and searching for your package.

## 5. (Optional) Install the Updated Package Locally
If you want to test the newly uploaded version locally, you can install it using:

```bash
pip install your-package-name --upgrade
```

## Summary of Commands:
1. **Update version in `setup.py`**
2. **Rebuild the package:**
   ```bash
   python setup.py sdist bdist_wheel
   ```
3. **Upload to PyPI:**
   ```bash
   twine upload dist/*
   ```
4. **Verify the upload on PyPI**
