from setuptools import setup


import pptx_template


def read(filename):
    with open(filename, 'r', encoding='utf-8') as myfile:
        return myfile.read()

setup(name='pptx-template-simple',
    version=pptx_template.__version__,
    description='The PowerPoint presentation builder using template.pptx (without support in cli)',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/Thykof/pptx-template',
    author='Thykof',
    author_email='thykof@protonmail.ch',
    install_requires=read('requirements.txt').split(),
    license='Apache-2.0',
    packages=['pptx_template'],
    test_suite='test',
    keywords=['powerpoint', 'ppt', 'pptx', 'template'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ]
)
