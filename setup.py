from setuptools import setup, find_packages

setup(
    name='youtube-scraper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    description='A simple YouTube video scraper.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/girmaneshir/youtube_scraper',  # Replace with your GitHub URL
    author='Girma N.',
    author_email='your.girma.neshir2015@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)