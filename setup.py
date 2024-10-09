from setuptools import setup, find_packages

# Read the content of your README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bio-wrangler",  # Your package name
    version="0.2",  # Package version, you can update this as needed
    author="Abdul-Rehman ikram",  # Replace with your name
    author_email="hanzo7n@gmail.com",  # Replace with your email
    description="A bioinformatics data wrangling package for FASTA, FASTQ, VCF, and GFF files.",
    long_description=long_description,  # This reads the README.md content
    long_description_content_type="text/markdown",  # Ensure PyPI displays the Markdown correctly
    url="https://github.com/se7en69/bio-wrangler",  # Replace with your GitHub repository URL
    project_urls={
        "Bug Tracker": "https://github.com/se7en69/bio-wrangler/issues",  # Replace with your issues URL
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[  # List your package dependencies here
        "pandas",
        "biopython",
        "gffutils",
        "pyvcf3",
    ],
    python_requires=">=3.6",  # Specify the Python versions your package supports
    include_package_data=True,  # Automatically include files listed in MANIFEST.in
    license="MIT",  # Specify the license type
)
