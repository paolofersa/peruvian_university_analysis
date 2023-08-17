import pandas as pd
from pathlib import Path

filepath = Path('df_prog_new.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)

# Load data
programa_df = pd.read_csv('df_prog.csv')

# Generate UNIVERSITIES MAP
# Name of departamentos
programa_df['LOCAL_LATITUD_UBICACION'] = programa_df['LOCAL_LATITUD_UBICACION'].str.replace(',', '.')
programa_df['LOCAL_LATITUD_UBICACION'] = programa_df['LOCAL_LATITUD_UBICACION'].astype(str)
programa_df['LOCAL_LONGITUD_UBICACION'] = programa_df['LOCAL_LONGITUD_UBICACION'].str.replace(',', '.')
programa_df['LOCAL_LONGITUD_UBICACION'] = programa_df['LOCAL_LONGITUD_UBICACION'].astype(str)
programa_df.to_csv(filepath, index=False)
