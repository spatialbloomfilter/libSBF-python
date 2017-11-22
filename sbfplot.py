"""
    Spatial Bloom Filter Python Library (libSBF-python)
    Copyright (C) 2017  Luca Calderoni, Dario Maio,
                        University of Bologna
    Copyright (C) 2017  Paolo Palmieri,
                        University College Cork

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
 """


import sbf
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

PLOT_PRECISION = 255


def sbfplot_areas_barchart(filter, title = 'Elements per set', show = True, save = True, format = 'pdf', filename = ''):
    """Plots the bar chart of the number of elements per area for a given filter.

    Plots the bar chart of the number of elements for each set of dataset the filter
    has been built on.

    Attributes:
        filter:     the SBF filter to plot
        title:      the plot title (default: 'Elements per set')
        show:       display the plot (default: True)
        save:       save the plot (default: True)
        format:     format of the plot: png, pdf, ps, eps or svg (default: 'pdf')
        filename:   the filname the plot should be saved as (default: '', but assigned
                    to sbfplot-elements-DATETIME.FORMAT in the function)
    """

    __sbfplot_check_args(filter, format)
    if (filename == ''):
        filename = 'sbfplot-elements-' + datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = filename + '.' + format

    x = list(range(1, filter.num_areas+1))
    y = [filter.area_members[i] for i in x]
    plt.bar(x, y)

    if not (filter.insert_file_list[0] == ''):
        title = title + ' (' + filter.insert_file_list[0] + ')'
    plt.title(title)
    plt.xlabel('Set')
    plt.ylabel('Members')
    plt.tight_layout()
    plt.grid(False)
    if (save):
        plt.savefig(filename)
        print('Plot saved as ' + filename)
    if (show):
        plt.show()
    plt.clf()


def sbfplot_cells(filter, expected = True, title = 'Cells', legend = 'upper left', show = True, save = True, format = 'pdf', filename = ''):
    """Plots the number of cells for the sets of a given filter.

    Plots the number of cells for the sets of the filter given as argument. If the
    respective arguments are true, also plots the a priori isep, the iser and the expected ise.

    Attributes:
        filter:         the SBF filter to plot
        expected:       plot the expected number of cells as well (default: True)
        potential:      plot the potential number of cells as well (default: True)
        title:          the plot title (default: 'Cells')
        show:           display the plot (default: True)
        save:           save the plot (default: True)
        format:         format of the plot: png, pdf, ps, eps or svg (default: 'pdf')
        filename:       the filname the plot should be saved as (default: '', but assigned
                        to sbfplot-cells-DATETIME.FORMAT in the function)
    """

    __sbfplot_check_args(filter, format)
    if (filename == ''):
        filename = 'sbfplot-cells-' + datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = filename + '.' + format

    x = list(range(1, filter.num_areas+1))
    #x = np.arange(1, filter.num_areas+1, round(filter.num_areas/PLOT_PRECISION))
    y = [filter.area_cells[i] for i in x]
    plt.bar(x, y, label='Cells')

    if (expected):
        if not hasattr(filter, 'area_expected_cells'):
            filter.expected_area_cells()
        y_exp = [filter.area_expected_cells[i] for i in x]
        plt.plot(x, y_exp, linewidth='0.8', color='red', label='Expected cells')

    legend = plt.legend(loc=legend)

    if not (filter.insert_file_list[0] == ''):
        title = title + ' (' + filter.insert_file_list[0] + ')'
    plt.title(title)
    plt.xlabel('Set')
    plt.ylabel('Cells')
    plt.tight_layout()
    plt.grid(False)
    if (save):
        plt.savefig(filename)
        print('Plot saved as ' + filename)
    if (show):
        plt.show()
    plt.clf()


def sbfplot_emersion(filter, expected = True, title = 'Emersion', legend = 'upper left', show = True, save = True, format = 'pdf', filename = ''):
    """Plots the emersion for a given filter.

    Plots the emersion value for the filter given as argument, over the number
    of sets the filter has been built on. If the respective argument is true,
    also plots the expected emersion.

    Attributes:
        filter:     the SBF filter to plot
        expected:   plot the expected emersion as well as the actual emersion
                    (default: True)
        title:      the plot title (default: 'Emersion')
        show:       display the plot (default: True)
        save:       save the plot (default: True)
        format:     format of the plot: png, pdf, ps, eps or svg (default: 'pdf')
        filename:   the filname the plot should be saved as (default: '', but assigned
                    to sbfplot-emersion-DATETIME.FORMAT in the function)
    """

    __sbfplot_check_args(filter, format)
    if (filename == ''):
        filename = 'sbfplot-emersion-' + datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = filename + '.' + format

    x = np.arange(1, filter.num_areas+1, round(filter.num_areas/PLOT_PRECISION))

    if (expected):
        y_exp = [filter.expected_area_emersion(i) for i in x]
        plt.plot(x, y_exp, color='red', label='Expected emersion')

    y = [filter.area_emersion(i) for i in x]
    plt.plot(x, y, label='Emersion')

    legend = plt.legend(loc=legend)

    if not (filter.insert_file_list[0] == ''):
        title = title + ' (' + filter.insert_file_list[0] + ')'
    plt.title(title)
    plt.xlabel('Set')
    plt.ylabel('Emersion')
    plt.tight_layout()
    plt.grid(True)
    if (save):
        plt.savefig(filename)
        print('Plot saved as ' + filename)
    if (show):
        plt.show()
    plt.clf()


def sbfplot_fpp(filter, apriori = True, non_elements_path = '', title = 'False positive probability', legend = 'upper right', show = True, save = True, format = 'pdf', filename = ''):
    """Plots the fpp for a given filter.

    Plots the false positive probability value for the filter given as argument,
    over the number of sets the filter has been built on. If the respective argument
    is true, also plots the a priori fpp. If a test file containing elements that
    are not part of the filter originating sets (non-elements) is given, the false
    positive rate is also calculated and plotted.

    Attributes:
        filter:         the SBF filter to plot
        apriori:        plot the a priori fpp as well as the actual isep (default: True)
        non_elements_path: plot the false positive rate calculated on the given
                        file (which must contain only elements that have not been
                        inserted in the filter) (default: '')
        title:          the plot title (default: 'False positive probability')
        show:           display the plot (default: True)
        save:           save the plot (default: True)
        format:         format of the plot: png, pdf, ps, eps or svg (default: 'pdf')
        filename:       the filname the plot should be saved as (default: '', but assigned
                        to sbfplot-fpp-DATETIME.FORMAT in the function)
    """

    __sbfplot_check_args(filter, format)
    if (filename == ''):
        filename = 'sbfplot-fpp-' + datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = filename + '.' + format

    x = np.arange(1, filter.num_areas+1, round(filter.num_areas/PLOT_PRECISION))

    if (apriori):
        if not hasattr(filter, 'area_apriori_fpp'):
            filter.compute_apriori_area_fpp()
        y_apriori = [filter.area_apriori_fpp[i] for i in x]
        plt.plot(x, y_apriori, color='red', label='A priori FPP')

    if not hasattr(filter, 'area_fpp'):
        filter.compute_area_fpp()
    y = [filter.area_fpp[i] for i in x]
    plt.plot(x, y, label='FPP')

    if not (non_elements_path == ''):
        filter.check_from_file(non_elements_path)
        area_results = [0]*(filter.num_areas + 1)
        for j in range(1, filter.num_areas + 1):
            area_results[j] = filter.check_results.count(j)
        y_iser = [area_results[i]/len(filter.check_results) for i in x]
        plt.plot(x, y_iser, color='C2', label='FPR')

    legend = plt.legend(loc=legend)

    if not (filter.insert_file_list[0] == ''):
        title = title + ' (' + filter.insert_file_list[0] + ')'
    plt.title(title)
    plt.xlabel('Set')
    plt.ylabel('FPP')
    plt.tight_layout()
    plt.grid(True)
    if (save):
        plt.savefig(filename)
        print('Plot saved as ' + filename)
    if (show):
        plt.show()
    plt.clf()


def sbfplot_isep(filter, apriori = True, iser = True, expected_ise = False, title = 'Inter-set errors', legend = 'upper right', show = True, save = True, format = 'pdf', filename = ''):
    """Plots the isep for a given filter.

    Plots the isep value for the filter given as argument, over the number
    of sets the filter has been built on. If the respective arguments are true,
    also plots the a priori isep, the iser and the expected ise.

    Attributes:
        filter:         the SBF filter to plot
        apriori:        plot the a priori isep as well as the actual isep (default: True)
        iser:           plot the iser (the actual error rate) (default: True)
        expected_ise:   plot the expected ise as well (default: False)
        title:          the plot title (default: 'Inter-set errors')
        show:           display the plot (default: True)
        save:           save the plot (default: True)
        format:         format of the plot: png, pdf, ps, eps or svg (default: 'pdf')
        filename:       the filname the plot should be saved as (default: '', but assigned
                        to sbfplot-isep-DATETIME.FORMAT in the function)
    """

    __sbfplot_check_args(filter, format)
    if (filename == ''):
        filename = 'sbfplot-isep-' + datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = filename + '.' + format

    x = np.arange(1, filter.num_areas+1, round(filter.num_areas/PLOT_PRECISION))

    if (apriori):
        if not hasattr(filter, 'area_apriori_isep'):
            filter.compute_apriori_area_isep()
        y_apriori = [filter.area_apriori_isep[i] for i in x]
        plt.plot(x, y_apriori, color='red', label='A priori ISEP')

    if not hasattr(filter, 'area_isep'):
        filter.compute_area_isep()
    y = [filter.area_isep[i] for i in x]
    plt.plot(x, y, label='ISEP')

    if (iser):
        if (not hasattr(filter, 'check_results')) or (not (isinstance(filter.check_results[0], str))):
            if (len(filter.insert_file_list) == 1):
                filter.check_from_file(filter.insert_file_list[0])
            else:
                raise ValueError("The current implementation of libsbfplot only works with filters built on a single insert file.")
        area_results = [0]*(filter.num_areas + 1)
        for j in range(0, len(filter.check_results)):
            if not (filter.check_results[j][0]):
                area_results[int(filter.check_results[j][1])] += 1
        y_iser = [area_results[i]/filter.area_members[i] for i in x]
        plt.plot(x, y_iser, color='C2', label='ISER')

    if (expected_ise):
        y_exp = [(filter.area_apriori_isep[i] * filter.area_members[i]) for i in x]
        plt.plot(x, y_exp, label='Expected ISE')

    legend = plt.legend(loc=legend)

    if not (filter.insert_file_list[0] == ''):
        title = title + ' (' + filter.insert_file_list[0] + ')'
    plt.title(title)
    plt.xlabel('Set')
    plt.ylabel('ISEP')
    plt.tight_layout()
    plt.grid(True)
    if (save):
        plt.savefig(filename)
        print('Plot saved as ' + filename)
    if (show):
        plt.show()
    plt.clf()

def sbfplot_safep(filter, title = 'A priori safeness probability', legend = 'upper left', show = True, save = True, format = 'pdf', filename = ''):
    """Plots the area safep for a given filter.

    Plots the area-specific a priori safeness probability value for the filter
    given as argument, over the number of sets the filter has been built on.

    Attributes:
        filter:         the SBF filter to plot
        title:          the plot title (default: 'A priori safeness probability')
        show:           display the plot (default: True)
        save:           save the plot (default: True)
        format:         format of the plot: png, pdf, ps, eps or svg (default: 'pdf')
        filename:       the filname the plot should be saved as (default: '', but assigned
                        to sbfplot-safep-DATETIME.FORMAT in the function)
    """

    __sbfplot_check_args(filter, format)
    if (filename == ''):
        filename = 'sbfplot-safep-' + datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = filename + '.' + format

    x = np.arange(1, filter.num_areas+1, round(filter.num_areas/PLOT_PRECISION))

    if not hasattr(filter, 'area_apriori_safep'):
        filter.compute_apriori_area_isep()
    y = [filter.area_apriori_safep[i] for i in x]
    plt.plot(x, y, label='SAFEP')

    legend = plt.legend(loc=legend)

    if not (filter.insert_file_list[0] == ''):
        title = title + ' (' + filter.insert_file_list[0] + ')'
    plt.title(title)
    plt.xlabel('Set')
    plt.ylabel('SAFEP')
    plt.tight_layout()
    plt.grid(True)
    if (save):
        plt.savefig(filename)
        print('Plot saved as ' + filename)
    if (show):
        plt.show()
    plt.clf()


def __sbfplot_check_args(filter, format):
    """ [Internal] Check the format and filename arguments

    [Internal] Check the format and filename arguments. This function is called
    by other library functions.

    Raises:
        AttributeError: The format argument is invalid.
        AttributeError: The filter argument is not an sbf object.
    """

    if (format not in ['png', 'pdf', 'ps', 'eps', 'svg']):
        raise AttributeError("Invalid format (it should be png, pdf, ps, eps or svg).")

    if (not isinstance(filter, sbf.sbf)):
        raise AttributeError("The filter passed as argument is not an SBF.")

    if (filter.members == 0):
        raise AttributeError("The filter passed as argument is empty.")
