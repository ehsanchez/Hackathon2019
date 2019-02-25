import imageio
import numpy
import subprocess


def display_time_series(time_series, iteration):
    """
    Display a time series

    :param time_series:
    :param iteration:
    """
    path = './time_series_%s.gif' % iteration
    with imageio.get_writer(path, mode='I', duration=0.5) as writer:
        for i in range(12):
            image = time_series[0, :, :, 4 * i:4 * i + 3]
            image = (255.0 * (image + 1.0) / 2.0).astype(numpy.uint8)
            writer.append_data(image)
    writer.close()
    return path


def display_gif(gif_path):
    """
    This function creates a process that displays the requiered gif

    :param gif_path: Path of the gif

    :return: the process that displays the gif
    """
    p = subprocess.Popen(["animate", gif_path])

    return p


def close_gif(gif_process):
    """
    Closes the gif process
    """
    gif_process.kill()
    return True