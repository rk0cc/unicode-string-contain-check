import setuptools

with open("README.md", "r") as readme_file:
    long_desc = readme_file.read()

setuptools.setup(
    name="UnicodeStringContainCheck",
    version="1.0.0",
    author="rk0cc",
    author_email="cyruschan1212@gmail.com",
    description="String contain validation for non-Latin language system",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/rk0cc/unicode-string-contain-check",
    package=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
    ],
    python_requires=">=3.8",
)