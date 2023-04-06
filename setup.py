import setuptools

with open('pypi_long_description.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name = "scikit-learn-wglasso",
    version = "0.0.1",
    description = "scikit-learn estimator for weighted glasso",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "Rush Han",
    packages = setuptools.find_packages(),
    install_requires = [
        "sklearn"
    ],
    url = "https://github.com/rushhan/weighted_glasso",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",  
        "Operating System :: POSIX :: Linux", 
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    python_requires= ">=3.6"
)