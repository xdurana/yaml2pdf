import setuptools

setuptools.setup(
    name="yaml2pdf",
    version="0.0.1",
    author="Xavier Duran",
    author_email="xavier.duran@pm.me",
    description="Simple PDF maker",
    long_description="Simple PDF maker from HTML"
    "templates and YAML data files",
    long_description_content_type="text/markdown",
    url="https://github.com/cancarner/yaml2pdf",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "WeasyPrint>=52.2",
        "pybars3>=0.9.7",
        "pyyaml>=5.3.1",
        "click>=7.1.2",
    ],
)
