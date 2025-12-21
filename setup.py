from setuptools import find_packages,setup
from typing import List

HYPONDOT_E = '-e .'
def get_requirements(file_path=str):
    '''this fucntion will retuen a list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n',"")for req in requirements]

    if HYPONDOT_E in requirements:
        requirements.remove(HYPONDOT_E)

setup(
name = "ml_project",
version='0.0.1',
author = "Viswa",
authon_email="vallabhanenivishwa11@gmail.com",
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)