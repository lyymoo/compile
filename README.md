## Compile
> Compiling Python source code into bytecode in production environment

## How To Use
```shell script
python -m compile -h  # help
python -m compile . -b -f  # Compile current directory
```

## 编译
> 将 python 源代码编译成供生产环境使用的机器字节码

## 如何使用
```shell script
python -m compile -h  # 帮助
python -m compile . -b -f  # 编译当前目录
```

[//]: <> (pypi.org)
[//]: <> (python -m pip install --user --upgrade setuptools wheel twine)
[//]: <> (python setup.py sdist bdist_wheel)
[//]: <> (python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*)
[//]: <> (python -m twine upload dist/*)
