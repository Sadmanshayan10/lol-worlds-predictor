import pandas as pd


def main():
    # Load the data
    file_path = '../data/raw/2025_LoL_esports_match_data_from_OraclesElixir.csv'
    df = pd.read_csv(file_path)

    print("=" * 50)
    print("LOL ESPORTS DATA EXPLORATION")
    print("=" * 50)

    # Basic info
    print(f"\n📊 Dataset Shape: {df.shape[0]:,} rows, {df.shape[1]:,} columns")

    # Column names
    print(f"\n📋 Columns ({len(df.columns)} total):")
    print(f"   {', '.join(df.columns[:10].tolist())}...")

    # First few rows
    print("\n🔍 First 5 rows:")
    print(df.head())

    # Data types
    print("\n📦 Data Types:")
    print(df.dtypes.value_counts())

    # Missing values
    print("\n❌ Missing Values (top 10):")
    print(df.isnull().sum().sort_values(ascending=False).head(10))

    # Check for key columns
    print("\n🎯 Key Columns Found:")
    key_cols = ['gameid', 'league', 'split', 'playoffs', 'patch', 'gamelength',
                'teamname', 'side', 'result', 'firstdragon', 'firstbaron', 'firsttower']

    found_cols = [col for col in key_cols if col in df.columns]
    missing_cols = [col for col in key_cols if col not in df.columns]

    print(f"   Found: {found_cols}")
    if missing_cols:
        print(f"   Missing: {missing_cols}")

    # Unique leagues
    if 'league' in df.columns:
        print("\n🏆 Leagues in Dataset:")
        print(f"   {df['league'].nunique()} unique leagues")
        print(f"   {sorted(df['league'].unique())[:10]}")

    # Sample stats
    print("\n📈 Quick Stats (numeric columns):")
    print(df.describe())

    print("\n" + "=" * 50)
    print("✅ Exploration Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
