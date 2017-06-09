from setuptools import setup

setup(
    name='python_urx',
    version='0.10.0',
    packages=["urx"],
    py_modules=[],
    install_requires=['setuptools'],
    author = "Olivier Roulet-Dubonnet",
    author_email = "olivier.roulet@gmail.com",
    maintainer='Adam Allevato',
    maintainer_email='allevato@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description=(
        "Python library to control an UR robot"
    ),
    license='GNU Lesser General Public License v3',
    entry_points={},
)
