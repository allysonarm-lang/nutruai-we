from setuptools import setup, find_packages

setup(
    name="nutruai",
    version="0.1.0",
    author="allysonarm-lang",
    author_email="dev@nutruai.io",
    description="Sistema inteligente de monitoramento nutricional com previsões",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/allysonarm-lang/nutruai-we",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0",
        "matplotlib>=3.5",
        "scikit-learn>=1.0",
        "numpy>=1.20",
    ],
    entry_points={
        "console_scripts": [
            "nutruai=nutruai.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    keywords="nutrição saúde IMC macronutrientes previsão",
    project_urls={
        "Bug Reports": "https://github.com/allysonarm-lang/nutruai-we/issues",
        "Source": "https://github.com/allysonarm-lang/nutruai-we",
    },
)
