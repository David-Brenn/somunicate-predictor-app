from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="soundpredictor",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for predicting sound characteristics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/David-Brenn/somunicate-predictor-app",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "librosa==0.10.2",
        "numpy==1.26.4",
        "pandas==2.2.2",
        "joblib==1.4.0",
        "scikit-learn==1.4.2",
        "mosqito==1.2.1",
        "streamlit==1.33.0",
        "torch==2.2.2",
        "torchmetrics==1.3.2",
        "pytorch_lightning==2.2.2",
        "matplotlib==3.8.4",
    ],
    entry_points={
        "console_scripts": [
            "soundpredictor=src.predict:main",
        ],
    },
)
