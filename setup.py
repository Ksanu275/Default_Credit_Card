from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirments(file_path:str)->List[str]:
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='Default_Credit_Card',
    version='0.0.1',
    author='Kumar Sanu',
    author_email='skuma275@gmail.com',
    install_requires=get_requirments('requirements.txt'),
    packages=find_packages()
)