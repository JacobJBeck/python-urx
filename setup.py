from setuptools import setup

setup(
    name='python_urx',
    version='0.11.0',
    description="Python library to control an UR robot",
    packages=['urx'],
    provides=['urx'],
    py_modules=[],
    install_requires=['setuptools', 'numpy', 'math3d'],
    author="Olivier Roulet-Dubonnet",
    author_email='olivier.roulet@gmail.com',
    maintainer="Jacob Beck",
    maintainer_email='beck@madeinspace.us',
    license="GNU Lesser General Public License v3",
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
    entry_points={},
)
