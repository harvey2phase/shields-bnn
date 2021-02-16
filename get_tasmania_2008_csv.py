import pandas as pd

PUBLIC_CSV_NAME = '~/Desktop/BENTHOZ_2015/BENTHOZ_2015_SECRET.csv'
TASMANIA_CSV_NAME = '~/Desktop/shields-bnn/tasmania-testing.csv'
CAMPAIGN_COL = 'campaign'
TASMANIA_CAMPAIGN = 'Tasmania 2008'

df = pd.read_csv(PUBLIC_CSV_NAME)
df.loc[df[CAMPAIGN_COL] == TASMANIA_CAMPAIGN].to_csv(
    TASMANIA_CSV_NAME, index = False,
)
