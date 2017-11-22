# libSFB-python #
libSBF - implementation of the Spatial Bloom Filters in Python

## Synopsis ##
The Spatial Bloom Filters (SBF) are a compact, set-based data structure that extends the original Bloom filter concept. An SBF represents and arbitrary number of sets, and their respective elements (as opposed to Bloom filters, which represent the elements of a single set). SBFs are particularly suited to be used in privacy-preserving protocols, as set-membership queries (i.e. the process of verifying if an element is in a set) can be easily computed over an encrypted SBF, through (somewhat) homomorphic encryption.

## Usage ##
Spatial Bloom Filters have been first proposed for use in location-privacy application, but have found application in a number of domains, including network security and the Internet of Things.

The libSBF-python repository contains the Python implementation of the SBF data structure. The SBF class is provided, as well as various methods for managing the filter:
- once the filter is constructed, the user can insert elements into it through the `insert` method. The `check` method, on the contrary, is used to verify weather an element belongs to one of the mapped sets. Two additional methods, `insert_from_file` and `check_from_file` can be used to insert and check elements from a CSV file.
- methods such as `filter_sparsity`, `filter_fpp`, `compute_area_fpp`, `compute_apriori_area_fpp`, `compute_area_isep`, `compute_apriori_area_isep`, `expected_area_emersion` and `area_emersion` allow to compute and return several probabilistic properties of the constructed filter.
- finally, two methods are provided to print out the filter: `print_filter` prints the filter and related statistics to the standard output, whereas `save_filter` writes the filter onto a CSV file.

For more details on the implementation, and how to use the library please refer to the [homepage](http://sbf.csr.unibo.it/ "SBF project homepage") of the project.

The library and the test application can be tested using the [sample datasets](https://github.com/spatialbloomfilter/libSBF-testdatasets "libSBF-testdatasets") provided in a separate repository.

A [C++ implementation](https://github.com/spatialbloomfilter/libSBF-cpp "libSBF-cpp") is also available. 

## Bibliography ##
The SBFs have been proposed in the following research papers:
- Luca Calderoni, Paolo Palmieri, Dario Maio: *Location privacy without mutual trust: The spatial Bloom filter.* Computer Communications, vol. 68, pp. 4-16, September 2015. ISSN 0140-3664. [DOI](http://dx.doi.org/10.1016/j.comcom.2015.06.011 "DOI")
- Paolo Palmieri, Luca Calderoni, Dario Maio: *Spatial Bloom Filters: Enabling Privacy in Location-aware Applications*. In: Inscrypt 2014. Lecture Notes in Computer Science, vol. 8957, pp. 16–36, Springer, 2015. [DOI](http://dx.doi.org/10.1007/978-3-319-16745-9_2 "DOI")

## Authors ##
Luca Calderoni, Dario Maio - University of Bologna (Italy)

Paolo Palmieri - University College Cork (Ireland)

## License ##
The source code is released under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. Please refer to the included files [COPYING](COPYING) and [COPYING.LESSER](COPYING.LESSER).

## Acknowledgements ##
This project uses several Python modules and in particular: hashlib, numpy, base64, csv, sys.
