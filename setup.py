from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="prepaid-card-manager",
    version="1.0.0",
    author="Prepaid Solutions Team",
    author_email="dev@prepaidcardmanager.com",
    description="Comprehensive prepaid card management tool for retail stores",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/prepaid-card-manager",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Office/Business :: Financial",
        "Topic :: Terminals",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "prepaid-manager=prepaid_manager.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "prepaid_manager": ["templates/*.txt", "config/*.json"],
    },
)
