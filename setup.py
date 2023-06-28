import setuptools

install_deps = ['numpy>=1.16', 
                'scipy',
                'matplotlib',
                'natsort', 
                'numba>=0.43.1',
                'opencv-python-headless', 
                'scikit-image',
                'pyqtgraph==0.12.0',
                'pyqt5==5.15.6', 
                'pyqt5.sip',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jarafacemap",
    license="GPLv3",
    version="0.2.0",
    author="Santiago Jaramillo (original authors: Carsen Stringer & Atika Syeda & Renee Tung)",
    author_email="sjara@uoregon.edu",
    description="Fork of Facemap v0.2.0 with additional measurements",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires = install_deps,
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
)
