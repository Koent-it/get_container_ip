from setuptools import setup, find_packages

setup(
  name='get_container_ip',
  packages=find_packages(include=['get_container_ip', 'get_container_ip.*']),
  install_requires=[
    'argparse',
    'logging',
  ],
  author='Koent S.r.l.',
  author_email='tools@koent.it',
  description='Un package per ottenere l\'indirizzo IP di un container.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/Koent-it/get_container_ip',
)