from setuptools import setup


with open('README.md') as f:
    long_description = f.read()


setup(
    name='mailtest',
    version='2.0.0',
    description="A unit testing tool for code that sends email. "
                "Flask-based version of https://github.com/keredson/mailtest",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Derek Anderson',
    author_email='public@kered.org',
    url='https://github.com/ConsenSys/mailtest-flask',
    packages=[],
    py_modules=['mailtest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)

