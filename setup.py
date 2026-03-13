""""
The setup.py file is an essential part of packaging and distributing Python projects.
It is used by setuptools(or distutils in older python version) to define the configuration of your project, such as metadata, dependencies, and more.
"""


from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This Function will return list of requirements
    """
    requirements_list:List[str] = []

    try:
        # Open and read the requirements.txt file
        with open("requirements.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)

    except FileNotFoundError:
        print("requirement.txt file not found")


    return requirements_list


print(get_requirements)
setup(
    name= "AI-Trip-Planner",
    version = "0.0.1",
    author = "Yashar Ghaffari",
    author_email="yashar1378.ghaffari@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
    )