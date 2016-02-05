import struct
import numpy as np
import matplotlib.pylab as plt


# TODO: Add verification tests about the file structure!
def read_bin_file(fname):
    """ Read CARLsim spikes output binary file.

        Params:
            fname (str): Input filename

        Returns:
            fileContent (str): The contents of the file in bits
    """
    with open(fname, 'rb') as file:
        fileContent = file.read()
    return fileContent


def convert_carlbin_2_human(bin_pattern):
    """ Convert CARLsim data string into human readable format.

        Params:
            bin_pattern (str): Input string containing data

        Returns:
            head (list): The header of CARLsim spikes output file
            body (list): The body of CARLsim spikes output file
    """
    import sys

    int_size = sys.getsizeof('i')//8
    size, h_size = len(bin_pattern), 5
    body_size = (size - (h_size*int_size))//int_size

    header = struct.unpack('i' * h_size, bin_pattern[:h_size*int_size])
    body = struct.unpack('i' * body_size, bin_pattern[20:])
    return body, header


def extract_times_neurons(data):
    """ Extract spikes times and neurons id labels from CARLsim
        raw data list.

        |----------------------|
        |1 | 3 | 5 | 6 | 4 | 7 |
        |----------------------|

        The first element is the first time that neuron number 3 --second
        element-- fires a spike. So this function reads a list like this 
        and stores the times and the neurons labels in two different lists.

        Params:
            data (list): Contains the actual data

        Returns:
            times (array): 1D Numpy array of spikes times
            neuron_id (array): 1D Numpy array of spiked neurons labels 
    """
    data = np.array(data)
    times = np.take(data, np.arange(0, data.shape[0], 2))
    neuron_id = np.take(data, np.arange(1, data.shape[0], 2))
    return times, neuron_id


def raster_plot(times, neuron_id):
    """ Plot a raster based on spikes times and neurons labels (id).

        Params:
            times (array): Numpy array of spikes times
            neuron_id (array): Numpy array of neurons labels (id)

        Returns:
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(times, neuron_id, '.k', alpha=.7, ms=0.5)
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('# Neuron')

    plt.show()

if __name__ == '__main__':
    bin_data = read_bin_file('spk_output.dat')
    data, _ = convert_carlbin_2_human(bin_data)
    times, neuron_id = extract_times_neurons(data)
    raster_plot(times, neuron_id)
