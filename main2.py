import csv

with open("YA_Books.csv", mode="r", encoding="utf-8") as bookfile:
    books = csv.reader(bookfile)
    next(books)

    earliest_year = 9999

    for row in books:
        if row[1].startswith("M"):
            print(row[1])

        year = int(row[2])
        if year < earliest_year:
            earliest_year = year
            most_recent_book = row


    print(f"Most recent book: \n{most_recent_book}")

    