from setuptools import setup


setup(
    name='envparse',
    version='0.1.0',
    url='https://github.com/rconradharris/envparse',
    license='MIT',
    author='Rick Harris',
    author_email='rconradharris@gmail.com',
    description='Environment Variable Parsing for Something Something',
    long_description=__doc__,
    py_modules=['envparse'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[''],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
