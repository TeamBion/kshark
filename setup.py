import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='kubectl-shark',  
     version='0.1',
     author="WoodProgrammer",
     description="Kubectl tcpdump handler",
     long_description=long_description,
     long_description_content_type="text/markdown",
      install_requires=[
          "pyyaml"
        ],
     url="https://github.com/WoodProgrammer/kubectl-tcpdumper/",
     packages=setuptools.find_packages(),
     entry_points ={
            'console_scripts': [
                'kubectl-shark = kshark.main:main'
            ]
        },
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )