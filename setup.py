# from distutils.core import setup, Extension
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pidng",
    include_package_data=True,
    version="4.0.9",
    author="Csaba Nagy",
    description="Python utility for creating Adobe DNG files from RAW image data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schoolpost/PiDNG",
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        "Topic :: Multimedia :: Graphics :: Capture :: Digital Camera",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires='>=3.6',
)