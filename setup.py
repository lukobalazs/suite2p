import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="suite2p",
    version="0.1.1",
    author="Marius Pachitariu and Carsen Stringer",
    author_email="marius10p at gmail.com",
    description="Pipeline for calcium imaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MouseLand/suite2p",
    packages=setuptools.find_packages(),
	install_requires = ['pyqtgraph', 'PyQt5', 'numpy', 'scipy', 'h5py'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
)