from setuptools import setup, find_packages
from typing import List
def get_requirements() -> List[str]:
    list_requirements:List[str]=[]
    return list_requirements


setup(
    name='Sensor_project',
    version='1.6.3',
    author="Arjun",
    author_email="arjun225553@gmail.com",
    packages=find_packages(),
    install_reuires=get_requirements(),
)
