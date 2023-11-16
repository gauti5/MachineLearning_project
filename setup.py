import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME = "End to End Machine Learning Project wth MLFLOW"
AUTHOR_USER_NAME ="Sandeep"
SRC_REPO="MLProject"
AUTHOR_EMAIL="sndpgauti@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Small Python Package for Ml App",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    };
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")


)