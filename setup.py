import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aversine",
    version="0.0.1",
    author="Babatope Ajepe",
    author_email="babatopeajepe@gmail.com",
    description="""Python implementation of haversine formula to determine the
    great-circle distance between two points on a sphere given their 
    longitudes and latitudes.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ajepe/haversine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
