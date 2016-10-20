from setuptools import setup, find_packages

# parse requirements
req_lines = [line.strip() for line in open(
    'requirements.txt').readlines()]
install_reqs = list(filter(None, req_lines))

libdir = 'py'
packages = find_packages(libdir)

setup(
    name="flexswitchV2",
    version="0.2.0",
    author="www.snaproute.com",
    author_email="support@snaproute.com",
    description=("SnapRoute FlexSwitch Python wrapper library"),
    license="Apache 2.0",
    keywords="networking automation",
    package_dir={'': libdir},
    packages=packages,
    install_requires=install_reqs,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
    ],
)
