from setuptools import setup
from glob import glob
import os

package_name = 'system_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='leo001xd',
    maintainer_email='leo001xd@example.com',
    description='Launch all system nodes',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={},
)

