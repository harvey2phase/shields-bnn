import pandas as pd

PUBLIC_CSV_NAME = '~/Desktop/BENTHOZ_2015/BENTHOZ_2015_PUBLIC.csv'
TASMANIA_CSV_NAME = '~/Desktop/shields-bnn/tasmania-2008.csv'
CAMPAIGN_COL = 'campaign'
TASMANIA_CAMPAIGN = 'Tasmania 2008'

public_df = pd.read_csv(PUBLIC_CSV_NAME)
public_df.loc[public_df[CAMPAIGN_COL] == TASMANIA_CAMPAIGN].to_csv(
    TASMANIA_CSV_NAME, index = False,
)
