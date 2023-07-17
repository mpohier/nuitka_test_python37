# Always prefer setuptools over distutils
from setuptools import setup, find_namespace_packages
from setuptools.command.sdist import sdist
import os
import pkg_resources
from shutil import move
from platform import (
    machine,
    system,
    python_implementation,
    python_version_tuple
)


class CustomSdist(sdist):
    """
    Class CustomSdist
    Used to compile into a single so
    """
    # Override the user options to be able to add ours
    sdist.user_options.append(
        ('no-compile', None, "Do not compile package with nuitka [default: compiled]")
    )

    @property
    def compile(self) -> bool:
        """ Property to manipulate the `no_compile` option.

        Returns:
            bool: `True` if the compilation with nuitka requested, `False` otherwise.
        """
        return not bool(self.no_compile)

    def initialize_options(self):
        """ Set or (reset) all options/attributes/caches used by the command to their default values.
        Note that these values may be overwritten during the build.
        """
        self.no_compile = None
        sdist.initialize_options(self)

    def finalize_options(self):
        """ Set final values for all options/attributes used by the command.
        Most of the time, each option/attribute/cache should only be set if it does not have any value yet.
        """
        if self.compile:
            print("Parameter `no-compile` not set, Nuitka compilation enabled.")
        else:
            print("Parameter `no-compile` set, Nuitka compilation disabled.")
        sdist.finalize_options(self)

    def run(self):
        """ Overridde the `sdist` command to compile the code of this module with Nuitka.
        The compilation is set by default BUT may be disabled by adding the option `no-compile`.
        Compilation steps:
        1. Nuitka is REQUIRED so verify if it is installed and raise a warning if the version does not match
        2. Use Nuitka to compile the code from `app.py`
        3. Embed the Nuitka result (`.so` and its associated `.pyi`)
        4. Run the parent sdist command
        """
        try:
            if self.compile:
                package_name = 'nuitka'
                try:
                    pkg_resources.get_distribution(package_name)
                except pkg_resources.DistributionNotFound:
                    print(f"\nERROR : Nuitka not installed, please install it and retry.\n")
                    return
                # Compile the `app.py`
                sub_dirs = ["mypackage", "demo"]
                os.system(
                    "python3 -m nuitka --module {module} --unstripped --trace-execution --follow-import-to={follow_import_to}".format(
                        module=os.path.join(os.path.dirname(__file__), *sub_dirs, "app.py"),
                        follow_import_to=".".join(sub_dirs)
                    )
                )
                # Copy the result in source
                expected_results = [
                    "app.pyi",
                    f"app.{python_implementation().lower()}-"
                    f"{''.join((python_version_tuple())[:-1])}m-"
                    f"{machine()}-{system().lower()}-gnu.so"
                ]
                for expected_result in expected_results:
                    move(expected_result, os.path.join(os.path.dirname(__file__), *sub_dirs, expected_result))
            # Call parent sdist
            sdist.run(self)
        # Be sure to restore environment and files at the end
        finally:
            print("compilation done")


REQUIREMENTS = [
]


setup(
    name='demo-package',
    version='0.0.0',
    description='description',
    long_description='long_description',
    url='url',
    author='author',
    author_email='author_email',
    python_requires='>=3.7',
    packages=find_namespace_packages(include=['mypackage.*']),
    namespace_packages=['mypackage'],
    include_package_data=True,
    install_requires=REQUIREMENTS,
    cmdclass={'sdist': CustomSdist},
    # Classifiers help users find your project by categorizing it.
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],
)
