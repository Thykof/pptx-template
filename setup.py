from setuptools import setup


import pptx_template


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='pptx-template-simple',
    version=pptx_template.__version__,
    description='The PowerPoint presentation builder using template.pptx (without support in cli)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Thykof/pptx-template',
    author='Thykof',
    author_email='thykof@protonmail.ch',
    license='Apache-2.0',
    packages=['pptx_template'],
    test_suite='test',
    install_requires=['python-pptx==0.6.18', 'pandas>=0.18.0', 'openpyxl>=2.4.7', 'six==1.12.0'],
    keywords=['powerpoint', 'ppt', 'pptx', 'template'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ]
)
