import setuptools



setuptools.setup(
    name="cdk_docker_sample",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description="An empty CDK Python app" ,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "cdk_docker_sample"},
    packages=setuptools.find_packages(where="cdk_docker_sample"),

    install_requires=[
        "aws-cdk.core==1.112.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
