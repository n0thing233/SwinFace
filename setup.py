from setuptools import setup, find_packages

setup(
    name='swinface',
    version='0.1.0',
    description='SwinFace fork',
    author='Adam Li',
    author_email='adamli19891123@gmail.com',
    url='https://github.com/n0thing233/SwinFace',
    packages=find_packages(),
    install_requires=[
        "timm",
        "torch==2.0.0",
        "torchvision==0.15.1",
        "opencv-python-headless",
        "tensorboard",
        "numpy==1.23",
        "pandas",
        "mxnet",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9.0',
)