import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compile",
    version="1.0.3",
    author="moz",
    author_email="m@lee.mo.cn",
    description="Compiling Python source code into bytecode in production environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lyymoo/compile",
    py_modules=["compile"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "twine.registered_commands": [
            "upload = twine.commands.upload:main",
            "register = twine.commands.register:main",
        ],
        "console_scripts": [
            "compile = compile:main",
        ],
    },
)
