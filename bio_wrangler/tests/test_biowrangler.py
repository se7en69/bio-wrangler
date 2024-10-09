import pytest
import pandas as pd
from bio_wrangler.bio_wrangler import BioWrangler

# Sample test data paths
FASTA_FILE = 'tests/data/sample.fasta'
VCF_FILE = 'tests/data/sample.vcf'
GFF_FILE = 'tests/data/sample.gff'
FASTQ_FILE = 'tests/data/sample.fastq'

@pytest.fixture
def bio_wrangler():
    """Fixture to initialize the BioWrangler class"""
    return BioWrangler()

def test_load_fasta(bio_wrangler):
    """Test loading a FASTA file"""
    data = bio_wrangler.load_fasta(FASTA_FILE)
    assert isinstance(data, pd.DataFrame)
    assert 'sequence' in data.columns
    assert len(data) > 0

def test_load_fastq(bio_wrangler):
    """Test loading a FASTQ file"""
    data = bio_wrangler.load_fastq(FASTQ_FILE)
    assert isinstance(data, pd.DataFrame)
    assert 'sequence' in data.columns
    assert 'quality' in data.columns
    assert len(data) > 0

def test_filter_fastq_by_quality(bio_wrangler):
    """Test filtering FASTQ data by quality"""
    data = bio_wrangler.load_fastq(FASTQ_FILE)
    filtered_data = bio_wrangler.filter_fastq_by_quality(data, 30.0)
    assert isinstance(filtered_data, pd.DataFrame)
    assert len(filtered_data) < len(data)  # Ensure some sequences are filtered

def test_summarize_fastq(bio_wrangler):
    """Test summarizing FASTQ data"""
    data = bio_wrangler.load_fastq(FASTQ_FILE)
    summary = bio_wrangler.summarize_fastq(data)
    assert 'total_sequences' in summary
    assert 'mean_quality' in summary

def test_load_vcf(bio_wrangler):
    """Test loading a VCF file"""
    data = bio_wrangler.load_vcf(VCF_FILE)
    assert isinstance(data, pd.DataFrame)
    assert 'CHROM' in data.columns
    assert len(data) > 0

def test_load_gff(bio_wrangler):
    """Test loading a GFF file"""
    data = bio_wrangler.load_gff(GFF_FILE)
    assert isinstance(data, pd.DataFrame)
    assert 'seqid' in data.columns
    assert len(data) > 0

def test_filter_by_quality(bio_wrangler):
    """Test filtering VCF data by quality"""
    data = bio_wrangler.load_vcf(VCF_FILE)
    filtered_data = bio_wrangler.filter_by_quality(data, 50.0)
    assert isinstance(filtered_data, pd.DataFrame)
    assert len(filtered_data) < len(data)  # Ensure some data is filtered out

def test_filter_by_chromosome(bio_wrangler):
    """Test filtering VCF data by chromosome"""
    data = bio_wrangler.load_vcf(VCF_FILE)
    filtered_data = bio_wrangler.filter_by_chromosome(data, 'chr1')
    assert isinstance(filtered_data, pd.DataFrame)
    assert len(filtered_data) < len(data)

def test_filter_by_position_range(bio_wrangler):
    """Test filtering VCF data by position range"""
    data = bio_wrangler.load_vcf(VCF_FILE)
    filtered_data = bio_wrangler.filter_by_position_range(data, 100000, 500000)
    assert isinstance(filtered_data, pd.DataFrame)
    assert len(filtered_data) < len(data)

def test_filter_by_attribute(bio_wrangler):
    """Test filtering GFF data by attribute"""
    data = bio_wrangler.load_gff(GFF_FILE)
    filtered_data = bio_wrangler.filter_by_attribute(data, 'ID', 'gene1')
    assert isinstance(filtered_data, pd.DataFrame)
    assert len(filtered_data) < len(data)

def test_extract_columns(bio_wrangler):
    """Test extracting specific columns from VCF data"""
    data = bio_wrangler.load_vcf(VCF_FILE)
    extracted_data = bio_wrangler.extract_columns(data, ['CHROM', 'POS', 'QUAL'])
    assert isinstance(extracted_data, pd.DataFrame)
    assert extracted_data.columns.tolist() == ['CHROM', 'POS', 'QUAL']

def test_summarize_data(bio_wrangler):
    """Test summarizing VCF data"""
    data = bio_wrangler.load_vcf(VCF_FILE)
    summary = bio_wrangler.summarize_data(data)
    assert 'total_rows' in summary
    assert 'columns' in summary

def test_merge_datasets(bio_wrangler):
    """Test merging multiple datasets"""
    data1 = bio_wrangler.load_vcf(VCF_FILE)
    data2 = bio_wrangler.load_vcf(VCF_FILE)
    merged_data = bio_wrangler.merge_datasets(data1, data2)
    assert isinstance(merged_data, pd.DataFrame)
    assert len(merged_data) == len(data1) + len(data2)

def test_save_data(bio_wrangler, tmpdir):
    """Test saving a DataFrame to a file"""
    data = bio_wrangler.load_vcf(VCF_FILE)
    save_path = tmpdir.join('test_output.csv')
    bio_wrangler.save_data(data, str(save_path), 'csv')
    
    # Ensure the file is saved correctly
    loaded_data = pd.read_csv(str(save_path))
    assert len(loaded_data) == len(data)
