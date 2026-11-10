import csv
# comma separated value
import matplotlib.pyplot as plt
'''
after adding matplotlib YA GOTTA RUN THE FILE IN THE TERMINAL
idk why...
'''

with open("YA_Books.csv", mode="r", encoding="utf-8") as bookfile:
    # mode "r" means read
    # as bookfile means alias/nickname

    books = csv.reader(bookfile)
    # skip the header row
    next(books)

    # author col is at index 1
    earliest_year = 0         

    # FOR BAR CHART:
    x_book_titles = []
    y_ratings = []

    for row in books:
        # print out authors that start with "M"
        # if row[1].startswith("M"):
        #     print(row[1])

        # find most recent book (highest number)
        year = int(row[2])
        if year > earliest_year:
            earliest_year = year
            most_recent_book = row

        # get the book with the worst rating:


        # FOR BAR CHART:
        x_book_titles.append(row[0])
        y_ratings.append(row[6])


    print(f"Most recent book: \n{most_recent_book}")


# bar(x,y)
plt.bar(x_book_titles, y_ratings)
plt.show()