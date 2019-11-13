import setuptools

description = "Compiling Python source code into bytecode in production environment"

setuptools.setup(
    name="compile",
    version="1.1.1",
    author="moz",
    author_email="m@lee.mo.cn",
    description=description,
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/lyymoo/compile",
    packages=["."],
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
