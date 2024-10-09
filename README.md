## Bio-Wrangler

Bio-Wrangler is a Python package for bioinformatics data wrangling. It helps load, filter, merge, and summarize bioinformatics datasets from formats like FASTA, FASTQ, VCF, and GFF.

Table of Contents
Features
Installation
Usage
Loading Data
Filtering Data
Merging Datasets
Saving Data
Contributing
License
Features
Load FASTA, FASTQ, VCF, and GFF files into pandas DataFrames.
Filter datasets by quality, chromosome, position, and attributes.
Merge datasets for combined analysis.
Save the processed datasets to CSV or Excel formats.

Installation
To install Bio-Wrangler via PyPI:
pip install bio-wrangler

## Usage

1. Loading Data
You can load data from FASTA, FASTQ, VCF, and GFF files into pandas DataFrames.
from bio_wrangler.bio_wrangler import BioWrangler

# Initialize the class
wrangler = BioWrangler()

# Load a FASTA file
fasta_data = wrangler.load_fasta("path/to/sample.fasta")
print(fasta_data.head())

2. Filtering Data
You can filter datasets by quality, chromosome, or other attributes.
# Filter FASTQ data by average quality
filtered_fastq = wrangler.filter_fastq_by_quality(fastq_data, 30.0)
print(filtered_fastq.head())

3. Merging Datasets
Merge multiple datasets into one for combined analysis.
merged_vcf = wrangler.merge_datasets(vcf_data1, vcf_data2)
print(merged_vcf.head())

4. Saving Data
Save the filtered dataset to a CSV file.
wrangler.save_data(filtered_vcf, "filtered_vcf.csv", "csv")
Contributing
Contributions are welcome! Please see CONTRIBUTING.md for guidelines on how to contribute to this project.

License
This project is licensed under the MIT License. See the LICENSE file for details.