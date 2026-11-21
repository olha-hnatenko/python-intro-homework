import csv
clean_rows = []
skipped_rows = []
try:
    with open("../data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row_number, row in enumerate(reader, start=1):
            if None in row:
                skipped_rows.append(f"Row {row_number}: extra column detected — skipped")
                continue
            try:
                row["amount"] = float(row["amount"])
                clean_rows.append(row)

            except (ValueError, TypeError) as error:
                skipped_rows.append(
                f"Row {row_number}: {type(error).__name__} — "
                f"could not convert {row['amount']!r} to float"
                )
                continue

            except KeyError as error:
                skipped_rows.append(f"Row {row_number}: KeyError — missing column {error}")
                continue


            
        print("=== CSV Report ===")
        print(f"Rows attempted: {len(clean_rows) + len(skipped_rows)}")
        print(f"Rows parsed:    {len(clean_rows)}")
        print(f"Rows skipped:   {len(skipped_rows)}")
        print()
        print("Skipped rows:")
        for message in skipped_rows:
            print(f"  {message}")
        print()
        print("Clean data:")
        for row in clean_rows:
            print(f"  {row['name']} | {row['category']} | ${row['amount']:.2f}")

except FileNotFoundError:
    print("Error: \"messy_data.csv\" was not found. Please check the file path and try again.")