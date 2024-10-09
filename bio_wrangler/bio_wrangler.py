import pandas as pd
from Bio import SeqIO
import vcf
import gffutils
from typing import List, Dict, Union

class BioWrangler:
    def __init__(self):
        pass

    def load_fasta(self, file_path: str) -> pd.DataFrame:
        """
        Load a FASTA file and return a DataFrame containing sequence data.
        """
        sequences = []
        for record in SeqIO.parse(file_path, "fasta"):
            sequences.append({
                'id': record.id,
                'description': record.description,
                'sequence': str(record.seq)
            })
        return pd.DataFrame(sequences)

    def load_fastq(self, file_path: str) -> pd.DataFrame:
        """
        Load a FASTQ file and return a DataFrame containing sequence data and quality scores.

        Args:
            file_path (str): Path to the FASTQ file.

        Returns:
            pd.DataFrame: DataFrame with columns ['id', 'sequence', 'quality'].
        """
        sequences = []
        for record in SeqIO.parse(file_path, "fastq"):
            sequences.append({
                'id': record.id,
                'sequence': str(record.seq),
                'quality': record.letter_annotations["phred_quality"]
            })
        return pd.DataFrame(sequences)

    def filter_fastq_by_quality(self, data: pd.DataFrame, quality_threshold: float) -> pd.DataFrame:
        """
        Filter FASTQ sequences based on an average quality score threshold.

        Args:
            data (pd.DataFrame): DataFrame containing FASTQ data with quality scores.
            quality_threshold (float): Minimum average quality score to filter by.

        Returns:
            pd.DataFrame: Filtered DataFrame containing sequences with average quality >= threshold.
        """
        # Calculate average quality for each sequence
        data['avg_quality'] = data['quality'].apply(lambda x: sum(x) / len(x) if len(x) > 0 else 0)
        return data[data['avg_quality'] >= quality_threshold]

    def summarize_fastq(self, data: pd.DataFrame) -> Dict:
        """
        Summarize key statistics of the FASTQ data.

        Args:
            data (pd.DataFrame): The DataFrame to summarize.

        Returns:
            Dict: A dictionary containing summary statistics.
        """
        summary = {
            'total_sequences': len(data),
            'mean_quality': data['quality'].apply(lambda q: sum(q) / len(q) if len(q) > 0 else 0).mean(),
            'min_quality': data['quality'].apply(lambda q: min(q) if len(q) > 0 else 0).min(),
            'max_quality': data['quality'].apply(lambda q: max(q) if len(q) > 0 else 0).max(),
        }
        return summary
    
    def load_vcf(self, file_path: str) -> pd.DataFrame:
        """
        Load a VCF file and return a DataFrame containing variant data.
        """
        vcf_reader = vcf.Reader(open(file_path, 'r'))
        records = []
        for record in vcf_reader:
            records.append({
                'CHROM': record.CHROM,
                'POS': record.POS,
                'ID': record.ID,
                'REF': record.REF,
                'ALT': [str(alt) for alt in record.ALT],
                'QUAL': record.QUAL,
                'FILTER': record.FILTER,
                'INFO': record.INFO
            })
        return pd.DataFrame(records)

    def load_gff(self, file_path: str) -> pd.DataFrame:
        """
        Load a GFF file and return a DataFrame containing feature data.
        """
        db = gffutils.create_db(file_path, dbfn=':memory:', force=True, keep_order=True, merge_strategy='merge', sort_attribute_values=True)
        records = []
        for feature in db.all_features():
            records.append({
                'seqid': feature.seqid,
                'source': feature.source,
                'type': feature.featuretype,
                'start': feature.start,
                'end': feature.end,
                'score': feature.score,
                'strand': feature.strand,
                'attributes': feature.attributes
            })
        return pd.DataFrame(records)

    def filter_by_quality(self, data: pd.DataFrame, quality_threshold: float) -> pd.DataFrame:
        """
        Filter VCF data based on a quality threshold.
        """
        return data[data['QUAL'] >= quality_threshold]

    def filter_by_chromosome(self, data: pd.DataFrame, chromosome: str) -> pd.DataFrame:
        """
        Filter data based on chromosome.
        """
        return data[data['CHROM'] == chromosome]

    def filter_by_position_range(self, data: pd.DataFrame, start_pos: int, end_pos: int) -> pd.DataFrame:
        """
        Filter data based on position range.
        
        Args:
            data (pd.DataFrame): DataFrame containing VCF or GFF data.
            start_pos (int): Starting position.
            end_pos (int): Ending position.
        
        Returns:
            pd.DataFrame: Filtered DataFrame.
        """
        return data[(data['POS'] >= start_pos) & (data['POS'] <= end_pos)]

    def filter_by_attribute(self, data: pd.DataFrame, attribute: str, value: str) -> pd.DataFrame:
        """
        Filter GFF data by a specific attribute.
        
        Args:
            data (pd.DataFrame): DataFrame containing GFF data.
            attribute (str): The attribute to filter by (e.g., 'gene_id').
            value (str): The value of the attribute to filter.
        
        Returns:
            pd.DataFrame: Filtered DataFrame.
        """
        return data[data['attributes'].apply(lambda x: attribute in x and value in x[attribute])]

    def extract_columns(self, data: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Extract specific columns from a DataFrame.
        
        Args:
            data (pd.DataFrame): The DataFrame to extract columns from.
            columns (List[str]): List of column names to extract.
        
        Returns:
            pd.DataFrame: DataFrame containing only the specified columns.
        """
        return data[columns]

    def summarize_data(self, data: pd.DataFrame) -> Dict:
        """
        Summarize key statistics of the loaded data.
        
        Args:
            data (pd.DataFrame): The DataFrame to summarize.
        
        Returns:
            Dict: A dictionary containing summary statistics.
        """
        summary = {
            'total_rows': len(data),
            'columns': data.columns.tolist()
        }
        if 'QUAL' in data.columns:
            summary['mean_quality'] = data['QUAL'].mean()
        if 'sequence' in data.columns:
            summary['total_sequences'] = len(data)
        if 'POS' in data.columns:
            summary['min_position'] = data['POS'].min()
            summary['max_position'] = data['POS'].max()
        
        return summary

    def merge_datasets(self, *datasets: pd.DataFrame) -> pd.DataFrame:
        """
        Merge multiple datasets into a single unified DataFrame.
        """
        return pd.concat(datasets, ignore_index=True)

    def save_data(self, data: pd.DataFrame, file_path: str, file_format: str = 'csv') -> None:
        """
        Save DataFrame to a file (CSV, Excel, etc.).
        
        Args:
            data (pd.DataFrame): DataFrame to save.
            file_path (str): Path to save the file.
            file_format (str): Format to save the file ('csv', 'xlsx', etc.).
        """
        if file_format == 'csv':
            data.to_csv(file_path, index=False)
        elif file_format == 'xlsx':
            data.to_excel(file_path, index=False)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")
