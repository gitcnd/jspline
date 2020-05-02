from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='jspline',
    version='1.0.2',
    description='Multi-dimensional parameterized spline curves (snappiness parameter gives uniform cubic B-splines, four-point subdivision splines, uniform quintic B-splines, and everything in-between)',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Chris Drake',
    author_email='cnd@geek.net.au',
    keywords=['J-Spline', 'spline', 'B-spline', 'curves', 'interpolation'],
    url='https://github.com/gitcnd/jspline',
    download_url='https://pypi.org/project/jspline/'
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
