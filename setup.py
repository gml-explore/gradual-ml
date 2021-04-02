import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gradual-ml-gmlExplore", # Replace with your own username
    version="1.0.0",
    author="gml team",
    author_email="gmlexplore@gmail.com",
    description="gradual-ml is a Python package that provides for Gradual Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gml-explore/gradual-ml",
    project_urls={
        "Bug Tracker": "https://github.com/gml-explore/gradual-ml/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)