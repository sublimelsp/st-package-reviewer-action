import os
import yaml


def read(name):
    """
    Reads a config file

    :param name:
        The name of the config file located in the config/ folder. The
        .yml suffix will automatically be added.

    :return:
        A dict of the settings
    """

    with open('%s/%s.yml' % (os.path.dirname(os.path.abspath(__file__)), name), 'r') as f:
        config = yaml.safe_load(f)

    return config
