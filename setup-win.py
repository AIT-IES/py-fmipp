import os
from setuptools import setup
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
  def is_pure(self):
    return False


# List of additional files (i.e., files without the '.py' extension) that are part of the distribution.
pyfmipp_additional_files = [
  'lib/_fmippim.pyd',
  'lib/_fmippex.pyd',
  'lib/fmippim.dll',
  'lib/fmippex.dll',
  'lib/sundials_cvode.lib',
  'lib/sundials_nvecserial.lib',
  'licenses/FMIPP_LICENSE.txt',
  'licenses/BOOST_SOFTWARE_LICENSE.txt',
  'licenses/SUNDIALS_LICENSE.txt',
  'export/bin/fmi2.dll',
  'export/bin/libfmipp_fmu_frontend.lib',
  'lib/boost_filesystem-vc141-mt-1_64.dll',
  'lib/boost_system-vc141-mt-1_64.dll'
  ]

  
# Read long description from file (reStructuredText syntax). Will be parsed and displayed as HTML online.
with open( 'README.txt' ) as file: pyfmipp_long_description = file.read()


# Specify the setup of this package.
setup(
  name = 'fmipp',
  version = '1.3',
  description = 'FMI++ Python Interface for Windows',
  #long_description = 'This package provides a Python wrapper for the FMI++ library, which \nintends to bridge the gap between the basic fuctionality provided by \nthe FMI specification and the typical requirements of simulation tools.',
  long_description = pyfmipp_long_description,
  url = 'http://fmipp.sourceforge.net',
  maintainer = 'Edmund Widl',
  maintainer_email = 'edmund.widl@ait.ac.at',
  license = 'BSD license & BOOST software license',
  platforms = 'Windows',
  keywords = [ 'FMI', 'Functional Mock-up Interface', 'FMI++ Library' ],
  classifiers=[
    'Development Status :: 4 - Beta',
	'Intended Audience :: Science/Research',
	'Operating System :: Microsoft :: Windows',
	'Topic :: Scientific/Engineering',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: C++',
	],
  packages = [ 'fmipp', 'fmipp.export' ],
  package_data = { 'fmipp': pyfmipp_additional_files },
  include_package_data=True,
  distclass=BinaryDistribution,
  )