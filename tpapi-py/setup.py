import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tpapi-py",
    version="0.1",
    author="Luke Knowles",
    author_email="luke.knowles@tierpoint.com",
    description="A Python wrapper for the TierPoint API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lukeknowles/tpapi-wrappers/",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)