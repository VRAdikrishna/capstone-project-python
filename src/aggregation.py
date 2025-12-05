def calculate_daily_totals(df):
    df = df.set_index('timestamp')
    return df.resample('D')['kwh'].sum()

def calculate_weekly_aggregates(df):
    df = df.set_index('timestamp')
    return df.resample('W')['kwh'].mean()

def building_wise_summary(df):
    summary = df.groupby('building')['kwh'].agg(['mean','min','max','sum'])
    summary = summary.rename(columns={'sum':'total_kwh'})
    return summary
