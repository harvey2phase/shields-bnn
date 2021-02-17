import pandas as pd

INPUT_CSV_NAME = '~/Desktop/shields-bnn/tasmania-training.csv'
OUTPUT_CSV_NAME = '~/Desktop/shields-bnn/waterfall-05.csv'
SELECT_COL = 'deployment'
SELECT_VAL = 'r20081006_231255_waterfall_05_transect'

df = pd.read_csv(INPUT_CSV_NAME)
df.loc[df[SELECT_COL] == SELECT_VAL].to_csv(
    OUTPUT_CSV_NAME, index = False,
)
