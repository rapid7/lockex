from setuptools import setup, find_packages
setup(name="lockex",
      version="0.2",
      description="Get lock from zookeeper and execute",
      packages=find_packages(exclude=["__pycache__"]),
      install_requires=['click==6.2', 'python_gflags==2.0', 'kazoo==2.2.1', 'psutil==4.1.0', 'future==0.15.2'],
      setup_requires=['flake8==2.5.4'],
      tests_require=['tox==2.3.1', 'pytest==2.6.3', 'testfixtures==4.9.1', 'mock==1.0.1'],
      entry_points={'console_scripts': ['lockex = lockex.execute:execute']},
      extras_require=dict(test=['testfixtures'],),
      license='BSD',)
