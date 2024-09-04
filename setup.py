from setuptools import setup

setup(name='dev_aberto_anandajgc',
      version='0.1',
      packages=['dev_aberto'],
      author='Ananda Campelo',
      install_requires=[
        'requests',
      ],
      classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
      ],
      python_requires='>=3.6',
      scripts=['scripts/hello.py'],
      )