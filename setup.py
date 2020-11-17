from setuptools import setup

with open("README.md","r") as readme_file:
    longdesc = readme_file.read()

setup(
    name='unicode_string_contain_check',
    version='2.0.0',
    description='String contain validation for non-Latin language system',
    long_description=longdesc,
    long_description_content_type="text/markdown",
    url='https://github.com/rk0cc/unicode-string-contain-check',
    author='rk0cc',
    author_email='cyruschan1212@gmail.com',
    license='Apache',
    packages=['unicode_string_contain_check'],
    zip_safe=False,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Filters"
    ],
)
