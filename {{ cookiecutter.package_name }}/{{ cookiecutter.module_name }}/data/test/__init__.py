from astropy.utils.data import get_pkg_data_filename


def get_test_filename(filename, **kwargs):
    """
    Return the full path to a test file in the ``data/test`` directory.

    Parameters
    ----------
    filename : `str`
        The name of the file inside the ``data/test`` directory.

    Return
    ------
    filepath : `str`
        The full path to the file.

    See Also
    --------

    astropy.utils.data.get_pkg_data_filename : Get package data filename

    Notes
    -----

    This is a wrapper around `astropy.utils.data.get_pkg_data_filename` which
    sets the ``package`` kwarg to be '{{ cookiecutter.module_name }}.data.test`.

    """
    return get_pkg_data_filename(filename, package="{{ cookiecutter.module_name }}.data.test", **kwargs)
