from setuptools import find_packages, setup

package_name = 'rincon_republisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/republisher.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='amilcar.rincon.charris@gmail.com',
    description='Republisher action example',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'republisher_server = rincon_republisher.republisher_server:main',
            'republisher_client = rincon_republisher.republisher_client:main',
        ],
    },
)
