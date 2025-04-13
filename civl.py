import pandas as pd
melbourne_file_path = 'https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/ef34bd55-86d8-4459-a710-79de30a45be2/download/traffic_density_202009.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data.describe()