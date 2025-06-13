import os
import setuptools

# Read the README file
with open('README.md', 'r') as fh:
    long_description = fh.read()

# Read requirements from setup directory
requirements = []
req_files = [
    'setup/requirements/requirements_base.txt',
    'setup/requirements/requirements_nuimages.txt', 
    'setup/requirements/requirements_tracking.txt'
    # 'setup/requirements/requirements_prediction.txt'  # Uncomment if needed
]

for req_file in req_files:
    if os.path.exists(req_file):
        with open(req_file) as f:
            requirements += [line.strip() for line in f.read().splitlines() if line.strip() and not line.startswith('#')]

def get_dirlist(_rootdir):
    dirlist = []
    with os.scandir(_rootdir) as rit:
        for entry in rit:
            if not entry.name.startswith('.') and entry.is_dir():
                dirlist.append(entry.path)
                dirlist += get_dirlist(entry.path)
    return dirlist

# Get subfolders recursively
rootdir = 'python-sdk'
packages = [d.replace('/', '.').replace('{}.'.format(rootdir), '') for d in get_dirlist(rootdir)]

# Filter out Python cache folders and egg-info
packages = [p for p in packages if not p.endswith('__pycache__') and not p.endswith('.egg-info')]

setuptools.setup(
    name='nuscenes-devkit',
    version='1.1.11',
    author='Holger Caesar, Oscar Beijbom, Qiang Xu, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, '
           'Sergi Widjaja, Kiwoo Shin, Caglayan Dicle, Freddy Boulton, Whye Kit Fong, Asha Asvathaman, Lubing Zhou '
           'et al.',
    author_email='nuscenes@motional.com',
    description='The official devkit of the nuScenes dataset (www.nuscenes.org).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nutonomy/nuscenes-devkit',
    python_requires='>=3.6',
    install_requires=requirements,
    packages=packages,
    package_dir={'': 'python-sdk'},
    package_data={'': ['*.json']},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    license='apache-2.0'
)
