from setuptools import find_packages, setup

from typing import List 
def get_requirements(file_path: str) -> List[str]:
   
   """
   this function will return the list of  requirments
   """
   requirements = []

   with open(file_path, "r") as file_obj:
       requirements = file_obj.readlines()
       requirements = [req.replace("\n", "") for req in requirements]

   return requirements

setup(
    name='Ml_Project',
    version='0.0.1',
    author='Durgesh',
    author_email='ravikose37@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
   
   