version = (0, 1, "dev6")

# version system
# major.minor.minute


def set_get_version():
    return "%d.%d.%d" % version


__version__ = set_get_version()
