try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='xtrmth',
    packages=find_packages(include=['xtrvar']),
    version='0.0.1',
    description="Every variable you could ever need. If this doesn't have it, nothing does.",
    long_description=long_description,
    author='William Nelson',
    license='MIT',
    install_requires=['xtrmth>=1.6.1'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: GPU',
        'Environment :: MacOS X',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: OpenStack',
        'Environment :: Other Environment',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.0'
)