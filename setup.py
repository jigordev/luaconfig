from setuptools import setup, find_packages

setup(
    name='luaconfig',
    version='0.1.0',
    description='LuaConfig is a powerful and easy-to-use Python library designed to read, manipulate and manage configuration files written in the Lua language.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='J. Igor Melo',
    author_email='jigordev@gmail.com',
    url='https://github.com/jigordev/luaconfig',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        "lupa==2.1",
        "PyYAML==6.0.1"
    ],
    include_package_data=True,
)