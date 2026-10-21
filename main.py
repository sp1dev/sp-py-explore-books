import csv
# comma separated value

with open("YA_Books.csv", mode="r", encoding="utf-8") as bookfile:
    # mode "r" means read
    # as bookfile means alias/nickname

    books = csv.reader(bookfile)
    # skip the header row
    next(books)

    # author col is at index 1
    earliest_year = 9999          # starts high so any real year is smaller

    for row in books:
        # print out authors that start with "M"
        # if row[1].startswith("M"):
        #     print(row[1])

        # print out last names (slice em up chat)
        # authorname = row[1]
        # lastindex = authorname.rfind(" ")
        # lastname = authorname[lastindex + 1:]
        # if lastname.startswith("J"):
        #     print(authorname)

        # find most recent book (highest number)
        year = int(row[2])
        if year < earliest_year:
            earliest_year = year
            most_recent_book = row

        # get the book with the worst rating:
        

    print(f"Most recent book: \n{most_recent_book}")

