import argparse
import pandas as pd

def main(csv_file, num_entries):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Extract relevant columns
    relevant_columns = ['PuzzleId', 'FEN', 'Moves', 'Rating', 'RatingDeviation', 'Popularity', 'NbPlays', 'Themes', 'GameUrl', 'OpeningTags']
    relevant_data = df[relevant_columns]

    # Print out the relevant information for the first few entries
    print(relevant_data.head(num_entries))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a Lichess puzzle CSV file.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file')
    parser.add_argument('--num_entries', type=int, default=5, help='Number of entries to display')
    args = parser.parse_args()

    main(args.csv_file, args.num_entries)
