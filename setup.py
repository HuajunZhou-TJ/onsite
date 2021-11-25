import setuptools 
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="onsite", 
    version="0.0.1",   
    author="Zhou Huajun",   
    author_email="1931314@tongji.edu.cn",   
    description="A tool packege for the competition of Onsite",
    long_description=long_description,    
    long_description_content_type="text/markdown",
    url="https://github.com/HuajunZhou-TJ/onsite", 
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=[
        'numpy',
        'shapely',
    ],
    python_requires='>=3.6',    #对python的最低版本要求
)