from setuptools import setup

setup(
    name = 'ComponentContribution',
    version = '1.0.0',
    author = 'Elad Noor',
    author_email='noor@imsb.biol.ethz.ch',
    description = 'Standard reaction Gibbs energy estimation for biochemical reactions',
    license = 'MIT',
    packages=['component_contribution'],
    url='https://github.com/eladnoor/component-contribution',
    install_requires=['scipy>=0.14.0',
                      'numpy>=1.6.2',
                      'oct2py==3.1.0'],
    data_files=[('TECRDB', ['data/TECRDB.tsv']),
                ('redox',  ['data/redox.tsv']),
                ('formation_energies_transformed', ['data/formation_energies_transformed.tsv']),
                ('equilibrator_compounds', ['data/equilibrator_compounds.json.gz']),
                ('kegg_additions', ['data/kegg_additions.json.gz']),
                ('kegg_compounds', ['data/kegg_compounds.json.gz']),
                ('cache', ['cache/compounds.json.gz'])
               ],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
    
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
    
        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',
    
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],
)

