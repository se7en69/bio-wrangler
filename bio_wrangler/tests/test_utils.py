# tests/test_utils.py
import pytest
import pandas as pd
from bio_wrangler.utils import chunked_file_reader, attributes_to_dataframe, vcf_alt_to_string, filter_data_by_column_value

@pytest.fixture
def sample_attributes():
    return {
        'ID': ['gene1'],
        'Name': ['Gene ABC'],
        'Description': ['A gene involved in XYZ']
    }

# Your test cases here...
def test_chunked_file_reader():
    """Test reading a large file in chunks"""
    file_path = 'tests/data/sample.fasta'
    chunks = list(chunked_file_reader(file_path, chunk_size=1024))
    assert len(chunks) > 0

def test_attributes_to_dataframe(sample_attributes):
    """Test converting attributes dictionary to DataFrame"""
    df = attributes_to_dataframe(sample_attributes)
    assert isinstance(df, pd.DataFrame)
    assert 'ID' in df.columns
    assert len(df) == 1

def test_vcf_alt_to_string():
    """Test converting VCF ALT field from list to string"""
    alt_field = ['A', 'T']
    alt_string = vcf_alt_to_string(alt_field)
    assert alt_string == 'A,T'

def test_filter_data_by_column_value():
    """Test filtering DataFrame by column value"""
    data = pd.DataFrame({
        'CHROM': ['chr1', 'chr2', 'chr1'],
        'POS': [100, 200, 300]
    })
    filtered_data = filter_data_by_column_value(data, 'CHROM', 'chr1')
    assert len(filtered_data) == 2
    assert all(filtered_data['CHROM'] == 'chr1')
