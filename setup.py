import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    #Here is the module name.
    name="dataVisualisation",

    #version of the module
    version="0.0.1",

    #Name of Author
    author="ramscodehub",

    #your Email address
    author_email="ywolf217@gmail.com",

    #Small Description about module
    description="Linear Regression",

    long_description=long_description,

    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(),

    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
