import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

reqs = []
setuptools.setup(
    name='gmm4torch',
    version='0.1',
    author='Lucas Deecke',
    description='Gaussian mixture models in PyTorch.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ldeecke/gmm-torch',
    license='MIT',
    install_requires=reqs,
    packages=setuptools.find_packages()
)
