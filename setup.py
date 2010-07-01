from distutils.core import setup
from xlink import __version__

setup(name='django-xlink',
    version=__version__,
    description='Django cross link searches particular sites for links back to your site and stores them',
    long_description=open('README.rst').read(),
    author='Justin Quick',
    author_email='justquick@gmail.com',
    url='http://github.com/justquick/django-xlink',
    packages=['xlink', 'xlink.management', 'xlink.management.commands'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
    )
