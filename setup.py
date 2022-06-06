from setuptools import find_packages, setup


packages = [
    "pytest<7,>=5",
    "pytest-timeout",
]

setup(
    name="drug-analyzer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=packages + ["wheel", "setuptools"],
    setup_requires=["pytest-runner"],
    tests_require=packages,
)