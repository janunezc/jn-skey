from setuptools import setup, find_packages

setup(
    name="jn-skey",  # Package name as it will appear on PyPI
    version="1.0.0",
    author="jnunezc",
    author_email="jose.a.nunez@gmail.com",
    description="A tool to type the current datetime when CTRL+D is pressed.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/janunezc/jn-skey",  # URL of your project, e.g., GitHub repo
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jn-skey=jn_skey.jn_skey:main',  # Command to run the package
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)