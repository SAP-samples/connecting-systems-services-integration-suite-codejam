# Connecting systems and services using SAP Integration Suite - Diagrams

So you are interested in checking out how the integration diagrams for this CodeJam were generated... The code for each diagram included in this repo will be under the `assets/diagrams/` folder for each exercise. Within it, you will find a *.py file containing the code and the output png.

The [*Creating architecture diagrams with code*](https://blogs.sap.com/2022/06/29/creating-architecture-diagrams-with-code/) blog post in SAP Community contains additional details on the icons included in the library used and sample scripts to generate diagrams.

**Want to get it running locally?**

Below are the steps required to run it on a Mac.

```bash
# Utilities
$ brew install virtualenvwrapper graphviz poetry

# Clone the forked repository
$ git clone git@github.com:ajmaradiaga/diagrams.git

# Switch to the directory
$ cd diagrams

# Switch to the sap-icons branch
$ git checkout sap-icons

# Build the project using poetry
$ poetry build

# Prepare your Python virtual environment
$ mkvirtualenv sap-diagrams

# Install the package in your virtual environment
$ poetry install --no-dev

# Now you can run one of scripts above locally. This will generate a png file with the output.
$ python tech-byte-diagram.py
```