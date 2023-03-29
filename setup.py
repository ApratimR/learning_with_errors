import setuptools

def readme():
    with open('readme.md') as f:
        return f.read()
    
setuptools.setup(
    name="LWE4",
    version="0.0.0.2",
    author="Apratim Ray",
    author_email="apratimr55@gmail.com",
    description="A Lattice based Asymetric public-key encryption algorithm based on learning with errors problem.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ApratimR/learning_with_errors",
    project_urls={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="LWE4"),
    py_modules=["LWE4"],
    python_requires=">=3.6",
)