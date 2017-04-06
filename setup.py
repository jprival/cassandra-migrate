from setuptools import setup

VERSION = '0.1'

setup(name='cassandra-migrate',
      packages=['cassandra_migrate'],
      version=VERSION,
      description='Simple Cassandra database migration program',
      url='https://github.com/Cobliteam/cassandra-migrate',
      download_url='https://github.com/Cobliteam/cassandra-migrate/archive/{}.tar.gz'.format(VERSION),
      author='Daniel Miranda',
      author_email='daniel@cobli.co',
      license='MIT',
      install_requires=[
          'cassandra-driver',
          'future',
          'pyyaml',
          'arrow',
          'click'
      ],
      scripts=['bin/cassandra-migrate'],
      keywords=['cassandra', 'schema', 'migration'])