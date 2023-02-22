
from distutils.core import setup
setup(
  name = 'riskii_spiders',         # How you named your package folder (MyLib)
  packages = ['riskii_spiders'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='GNU',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = '',   # Give a short description about your library
  author = 'Juan Cepeda',                   # Type in your name
  author_email = 'juancepeda.gestion@gmail.com',      # Type in your E-Mail
  url = '',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = [],   # Keywords that define your package best
  
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',   # Again, pick a license
    'Programming Language :: Python :: 3.11',
  ],
)