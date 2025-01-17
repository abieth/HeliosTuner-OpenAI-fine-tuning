from setuptools import setup, find_packages

setup(
    name='HeliosTuner',
    version='1.0.0',
    author='Errahum',
    description='A project for fine-tuning OpenAI models using HeliosTuner.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Errahum/HeliosTuner-OpenAI-fine-tuning',
    packages=find_packages(),
    install_requires=[
        'openai',
        'pydantic',
        'requests',
        'python-dotenv',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'heliostuner=main_heliostuner:main_heliostuner',
        ],
    },
    include_package_data=True,
    license='MIT',
)