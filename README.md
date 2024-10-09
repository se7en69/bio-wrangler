# Bio-Wrangler

**Bio-Wrangler** is a Python package designed for wrangling bioinformatics data, including formats such as **FASTA**, **FASTQ**, **VCF**, and **GFF**. The package allows users to load, filter, summarize, and merge bioinformatics datasets into pandas DataFrames, enabling efficient data manipulation and analysis.

## Features

- Load **FASTA**, **FASTQ**, **VCF**, and **GFF** files into pandas DataFrames.
- Filter data based on quality, chromosome, position, and attributes.
- Summarize datasets to extract key statistics.
- Merge multiple datasets.
- Save processed data to CSV or Excel formats.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Loading Data](#loading-data)
  - [Filtering Data](#filtering-data)
  - [Summarizing Data](#summarizing-data)
  - [Merging Datasets](#merging-datasets)
  - [Saving Data](#saving-data)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install Bio-Wrangler, use the following command:

pip install bio-wrangler


## Usage

### 1. Loading Data

Bio-Wrangler provides methods to load bioinformatics files into pandas DataFrames.

#### Example: Loading FASTA, FASTQ, VCF, and GFF Files

from bio_wrangler.bio_wrangler import BioWrangler

# Initialize the class
wrangler = BioWrangler()

# Load a FASTA file
fasta_data = wrangler.load_fasta('path/to/sample.fasta')
print(fasta_data.head())

# Load a FASTQ file
fastq_data = wrangler.load_fastq('path/to/sample.fastq')
print(fastq_data.head())

# Load a VCF file
vcf_data = wrangler.load_vcf('path/to/sample.vcf')
print(vcf_data.head())

# Load a GFF file
gff_data = wrangler.load_gff('path/to/sample.gff')
print(gff_data.head())


### 2. Filtering Data

Bio-Wrangler allows you to filter data based on various criteria such as quality, chromosome, position, and attributes.

#### Example: Filtering FASTQ by Quality

# Filter FASTQ data by average quality score threshold
filtered_fastq = wrangler.filter_fastq_by_quality(fastq_data, 30.0)
print(filtered_fastq.head())

#### Example: Filtering VCF by Chromosome

# Filter VCF data to retain only records from a specific chromosome
filtered_vcf = wrangler.filter_by_chromosome(vcf_data, 'chr1')
print(filtered_vcf.head())


#### Example: Filtering GFF by Attribute

# Filter GFF data by a specific attribute, such as gene_id
filtered_gff = wrangler.filter_by_attribute(gff_data, 'ID', 'gene1')
print(filtered_gff.head())


#### Example: Filtering VCF by Position Range

# Filter VCF data by a specific position range
filtered_vcf_range = wrangler.filter_by_position_range(vcf_data, 100000, 500000)
print(filtered_vcf_range.head())


### 3. Summarizing Data

Bio-Wrangler can generate summary statistics for your datasets.

#### Example: Summarizing FASTQ Data

# Summarize FASTQ data
fastq_summary = wrangler.summarize_fastq(fastq_data)
print(fastq_summary)


#### Example: Summarizing VCF Data

# Summarize VCF data
vcf_summary = wrangler.summarize_data(vcf_data)
print(vcf_summary)


### 4. Merging Datasets

Bio-Wrangler can merge multiple datasets into a single DataFrame.

#### Example: Merging VCF Datasets


# Merge two VCF datasets
merged_vcf = wrangler.merge_datasets(vcf_data, filtered_vcf)
print(merged_vcf.head())


### 5. Saving Data

After processing your data, you can save it to CSV or Excel formats using Bio-Wrangler.

#### Example: Saving Filtered VCF Data to CSV

# Save the filtered VCF data to a CSV file
wrangler.save_data(filtered_vcf, 'filtered_vcf_output.csv', 'csv')


#### Example: Saving Data to Excel

# Save data to an Excel file
wrangler.save_data(filtered_fastq, 'filtered_fastq_output.xlsx', 'xlsx')

## Contributing

Contributions to Bio-Wrangler are welcome! If you have any bug reports, feature requests, or pull requests, please follow the guidelines in the **CONTRIBUTING.md** file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
