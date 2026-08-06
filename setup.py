from setuptools import find_packages, setup

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kali',
    maintainer_email='kali@todo.todo',
    description='ROS2 Publisher, Subscriber and Turtle Square',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = my_robot.publisher:main',
            'subscriber = my_robot.subscriber:main',
            'turtle_square = my_robot.turtle_square:main',
        ],
    },
)
