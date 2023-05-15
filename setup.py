import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# Get requirements from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="hifi",
    version="5.0.0",
    author="Austin Brown",
    author_email="austinbrown34@gmail.com",
    description="Command-line tool to find nearest store.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/austinbrown34/hifi",
    packages=setuptools.find_packages(),
    scripts=['scripts/hifi', 'scripts/visbeats'],
    install_requires=required,
    include_package_data=True
)
