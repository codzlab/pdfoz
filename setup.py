import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstall(install):
    def run(self):
        install.run(self)
        if sys.platform == 'win32':
            self.create_shortcuts()

    def create_shortcuts(self):
        import shutil
        import winshell

        # Get the installation directory
        install_dir = self.install_scripts

        # Create a shortcut on the desktop
        desktop = winshell.desktop()
        shortcut_file = os.path.join(desktop, "PDF Reader.lnk")
        target = os.path.join(install_dir, "pdfoz.exe")
        icon = target  # You can specify an icon file if needed
        winshell.CreateShortcut(
            Path=shortcut_file,
            Target=target,
            Icon=(icon, 0),
            Description="PDF Reader"
        )

        # Create a shortcut in the start menu
        start_menu = winshell.programs()
        shortcut_file = os.path.join(start_menu, "PDFoz.lnk")
        winshell.CreateShortcut(
            Path=shortcut_file,
            Target=target,
            Icon=(icon, 0),
            Description="PDF Reader"
        )

setup(
    name='pdfoz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'pdf-reader=ui.main:main',
        ],
    },
    author='Codzlab',
    author_email='codzlabsio+github@gmail.com',
    description='A PDF reader application',
    license='MIT',
    keywords='pdf reader',
    url='https://github.com/codzlab/pdfoz',
    cmdclass={
        'install': CustomInstall,
    },
)
